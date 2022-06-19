from django.shortcuts import render
import csv
from mainapp.models import Victim
from email_list.models import EmailList
from django.http import HttpResponse
# Create your views here.

def import_csv(request, list_id):
    list = EmailList.objects.get(pk=list_id)

    if request.method == "POST":
        csv_file = request.FILES["csv_data"]
        print(csv_file.name.endswith('.csv'))

        file_data = csv_file.read().decode("utf-8")
        # print(file_data)
        lines = file_data.split("\n")
        # for line in lines:
        #     fields = line.split(",")

        reader = csv.DictReader(lines)
        for row in reader:
            try:
                v = Victim.objects.get(email=row['email'], list=list)
                v.email = row["email"]
                v.first_name = row["first_name"]
                v.last_name = row["last_name"]
                v.save()
            except Victim.DoesNotExist:
                v = Victim.objects.create(
                    email=row["email"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    list=list,
                )



    return render(request, 'backup/import.html', {'list':list})


def export_csv(request, list_id):
    list = EmailList.objects.get(pk=list_id)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="'+list.name+'.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'email'])
    for email in list.emails.all():
        writer.writerow([email.first_name, email.last_name, email.email])

    return response

    #return HttpResponse("Do not have permission!")



