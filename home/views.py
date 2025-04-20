from django.shortcuts import render
from django.http import JsonResponse
from .models import Draftee, Admin


def home(request):
    return render(request, "home/index.html")


def check_date(request, dateStr):
    month, day = map(int, dateStr.split("-"))
    records = Draftee.objects.filter(month=month, day=day).order_by("draftyear")
    admins = Admin.objects.all()

    if records:
        years = []
        explanations = []
        for record in records:
            if not record.draftnumber:
                continue
            draftnumber = int(record.draftnumber)

            for admin in admins:
                if not admin.maxcalled:
                    continue

                if int(record.draftyear) == int(admin.draftyear):
                    if draftnumber <= int(admin.maxcalled):
                        year = record.draftyear
                        years.append(year)

                        explanation = f"You were drawn number {draftnumber} out of the max of {admin.maxcalled} in {year}"
                        explanations.append(explanation)
                
        year_str = ", ".join(str(y) for y in years)
        explanation_str = ",".join(str(e) for e in explanations)

        if len(years) > 0:
            message = (
                f"You would have been drafted in the {year_str} draft"
                if len(years) == 1
                else f"You would have been drafted in the {year_str} drafts"
            )

            return JsonResponse(
                {
                    "title": "Drafted",
                    "message": message,
                    "explanations": explanation_str.split(','),
                }
            )
        else:
            return JsonResponse(
                {
                    "title": "Not drafted",
                    "message": "You would not have been drafted",
                }
            )
    else:
        return JsonResponse(
            {"title": "No date selected", "message": ""}
        )
