from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # SOLO PER TEST - RIMUOVILO SE FUNZIONA SENZA
def update_email(request):
    result = None
    message = None

    if request.method == "POST":
        poiid = request.POST.get("poiid")
        new_email = request.POST.get("email_nuova")

        if not poiid or not new_email:
            message = "Errore: ID POI e nuova email sono obbligatori!"
        else:
            try:
                update_query = """
                UPDATE subscription.poi 
                SET email_poc = %s  
                WHERE poiid = %s
                """
                select_query = """
                SELECT poiid, dealerid, email_poc
                FROM subscription.poi 
                WHERE poiid = %s
                """

                with connection.cursor() as cursor:
                    cursor.execute(update_query, [new_email, poiid])
                    connection.commit()
                    cursor.execute(select_query, [poiid])
                    result = cursor.fetchall()

                if result:
                    message = f"Email aggiornata con successo per POI ID {poiid}."
                else:
                    message = "Errore: POI ID non trovato nel database."

            except Exception as e:
                message = f"Errore nell'aggiornamento: {str(e)}"

    return render(request, "updater/update_email.html", {"message": message, "result": result})
