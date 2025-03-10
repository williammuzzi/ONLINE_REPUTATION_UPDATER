from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

# Home Page
def home(request):
    return render(request, "updater/index.html")

# Aggiorna Email
@csrf_exempt  # SOLO PER TEST - RIMUOVILO SE FUNZIONA SENZA
def update_email(request):
    result = None
    message = None

    if request.method == "POST":
        poiid = request.POST.get("poiid")
        new_email = request.POST.get("email_nuova")

        update_query = """
        UPDATE subscription.poi 
        SET email_poc = %s  
        WHERE poiid = %s
        """
        select_query = """
        SELECT poiid, dealerid, outletid, physicallocation, brand, main_brand, 
               email_poc, active, subscribed, timestamp_subscribed, ordered, 
               ordered_timestamp, rtgl, gmb_url, gmb_listing_name
        FROM subscription.poi 
        WHERE dealerid IN (SELECT DISTINCT dealerid FROM subscription.poi p WHERE poiid = %s)
        """

        with connection.cursor() as cursor:
            cursor.execute(update_query, [new_email, poiid])
            connection.commit()
            cursor.execute(select_query, [poiid])
            result = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        message = f"Email aggiornata con successo per POI ID {poiid}."

    return render(request, "updater/update_email.html", {"message": message, "result": result, "columns": columns if result else []})

# Aggiorna GMB
def update_gmb(request):
    result = None
    message = None

    if request.method == "POST":
        poiid = request.POST.get("poiid")
        new_gmb_url = request.POST.get("gmb_url")

        update_query = """
        UPDATE subscription.poi 
        SET gmb_url = %s  
        WHERE poiid = %s
        """
        select_query = """
        SELECT poiid, dealerid, outletid, physicallocation, brand, main_brand, 
               email_poc, active, subscribed, timestamp_subscribed, ordered, 
               ordered_timestamp, rtgl, gmb_url, gmb_listing_name
        FROM subscription.poi 
        WHERE dealerid IN (SELECT DISTINCT dealerid FROM subscription.poi p WHERE poiid = %s)
        """

        with connection.cursor() as cursor:
            cursor.execute(update_query, [new_gmb_url, poiid])
            connection.commit()
            cursor.execute(select_query, [poiid])
            result = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

        message = f"GMB URL aggiornato con successo per POI ID {poiid}."

    return render(request, "updater/update_gmb.html", {"message": message, "result": result, "columns": columns if result else []})

# Cambia POI (Placeholder)
def update_poi(request):
    message = "Funzione ancora da implementare."
    return render(request, "updater/update_poi.html", {"message": message})

# Daily Check
def daily_check(request):
    query = """
    SELECT
        CONCAT_WS(', ',
            IF(p.ordered = 1 AND (p.gmb_url IS NULL OR TRIM(p.gmb_url) = '' OR p.email_poc IS NULL OR TRIM(p.email_poc) = '' OR p.main_brand IS NULL OR TRIM(p.main_brand) = ''), 'MISSING GMB DATA', NULL),
            IF(p.subscribed = 1 AND (p.ordered IS NULL OR p.ordered = 0), 'SUBSCRIBED BUT NOT ORDERED', NULL),
            IF(p.subscribed = 1 AND p.timestamp_subscribed IS NULL, 'SUBSCRIBED BUT NO TIMESTAMP SUBSCRIBED', NULL)
        ) AS condition_description,
        p.poiid, p.dealerid, p.outletid, p.physicallocation, p.brand, p.main_brand, 
        p.email_poc, p.active, CAST(p.subscribed AS UNSIGNED) as Subscribed, p.timestamp_subscribed, 
        p.ordered, CAST(p.ordered_timestamp AS UNSIGNED) as ordered_timestamp, p.rtgl, p.gmb_url, p.gmb_listing_name
    FROM subscription.poi p
    WHERE (p.ordered = 1 AND (p.gmb_url IS NULL OR p.email_poc IS NULL OR p.main_brand IS NULL))
    OR (p.subscribed = 1 AND p.ordered = 0)
    OR (p.subscribed = 1 AND p.timestamp_subscribed IS NULL)
    ORDER BY p.dealerid;
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    return render(request, "updater/daily_check.html", {"columns": columns, "data": data})
