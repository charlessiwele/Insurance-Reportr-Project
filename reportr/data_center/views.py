import os.path

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from data_center.models import PaymentDocument, DocumentStatus, Report, GeneratedReport
from data_center.services.report_services import days_from_suspension_report, agent_collection_report, \
    payment_type_report, ReportTypes
from data_center.services.sync_payment_doc_agents import sync_payment_doc_agents
from data_center.services.sync_payment_doc_payments import sync_payment_doc_payments


# Create your views here.
class SyncDocumentPaymentsView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        sync_payment_result = sync_payment_doc_payments(kwargs.get('document_id'))
        new_process_status = DocumentStatus.objects.get(name='PROCESSED')
        document = PaymentDocument.objects.get(pk=kwargs.get('document_id'))
        document.process_status = new_process_status
        document.save()
        response = HttpResponse(str(sync_payment_result) + " Records Processed", content_type='text/html')
        return response


class SyncDocumentAgentsView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        sync_payment_result = sync_payment_doc_agents(kwargs.get('document_id'))
        new_process_status = DocumentStatus.objects.get(name='PROCESSED')
        document = PaymentDocument.objects.get(pk=kwargs.get('document_id'))
        document.process_status = new_process_status
        document.save()
        response = HttpResponse(str(sync_payment_result) + " Records Processed", content_type='text/html')
        return response


class GenerateReportsView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        report = Report.objects.get(pk=kwargs.get('report_id'))
        response = HttpResponse("No files Generated", content_type='text/html')

        if report.report_type.name == ReportTypes.days_from_suspension_report:
            suspension_report_path = days_from_suspension_report(kwargs.get('report_id'))
            GeneratedReport.objects.get_or_create(
                name=os.path.basename(suspension_report_path),
                description='days to suspension report',
                file=suspension_report_path,
                report=report
            )

            result = {
                'suspension_report_path': suspension_report_path
            }
            response = JsonResponse(result, safe=False)

        elif report.report_type.name == ReportTypes.payment_type_report:
            payment_type_report_path = payment_type_report(kwargs.get('report_id'))
            GeneratedReport.objects.get_or_create(
                name=os.path.basename(payment_type_report_path),
                description='payment type report',
                file=payment_type_report_path,
                report=report
            )

            result = {
                'payment_type_report_path': payment_type_report_path
            }
            response = JsonResponse(result, safe=False)

        elif report.report_type.name == ReportTypes.agent_collection_report:
            collection_report_path = agent_collection_report(kwargs.get('report_id'))
            GeneratedReport.objects.get_or_create(
                name=os.path.basename(collection_report_path),
                description='agen collections report',
                file=collection_report_path,
                report=report
            )

            result = {
                'collection_report_path': collection_report_path
            }
            response = JsonResponse(result, safe=False)

        elif report.report_type.name == ReportTypes.all_reports:
            suspension_report_path = days_from_suspension_report(kwargs.get('report_id'))
            payment_type_report_path = payment_type_report(kwargs.get('report_id'))
            collection_report_path = agent_collection_report(kwargs.get('report_id'))

            GeneratedReport.objects.get_or_create(
                name=os.path.basename(suspension_report_path),
                description='days to suspension report',
                file=suspension_report_path,
                report=report
            )

            GeneratedReport.objects.get_or_create(
                name=os.path.basename(collection_report_path),
                description='agen collections report',
                file=collection_report_path,
                report=report
            )

            GeneratedReport.objects.get_or_create(
                name=os.path.basename(payment_type_report_path),
                description='payment type report',
                file=payment_type_report_path,
                report=report
            )

            result = {
                'suspension_report_path': suspension_report_path,
                'collection_report_path': collection_report_path,
                'payment_type_report_path': payment_type_report_path
            }
            response = JsonResponse(result, safe=False)
        return response
