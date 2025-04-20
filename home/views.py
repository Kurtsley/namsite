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
        for record in records:
            draftnumber = int(record.draftnumber)

            for admin in admins:
                if not admin.maxcalled:
                    continue

                if int(record.draftyear) == int(admin.draftyear):
                    if draftnumber <= int(admin.maxcalled):
                        year = record.draftyear
                        years.append(year)

        year_str = ", ".join(str(y) for y in years)

        if len(years) > 0:
            message = (
                f"You would have been drafted in the {year_str} draft"
                if len(years) == 1
                else f"You would have been drafted in the {year_str} drafts"
            )

            return JsonResponse(
                {
                    "found": True,
                    "title": "Drafted",
                    "message": message,
                    "year_str": year_str,
                }
            )
        else:
            return JsonResponse(
                {
                    "found": False,
                    "title": "Not drafted",
                    "message": "You would not have been drafted",
                }
            )
    else:
        return JsonResponse(
            {"found": False, "title": "No date selected", "message": ""}
        )
