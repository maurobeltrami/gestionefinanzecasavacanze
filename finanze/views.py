# finanze/views.py

from django.shortcuts import render
from django.db.models import Sum, Avg
from .models import Transazione, RiepilogoMensile
from datetime import datetime
from decimal import Decimal # <--- 1. IMPORTA IL TIPO DECIMAL

def riepilogo_finanze(request):
    # --- 1. Calcolo del Mese Corrente (Transazioni) ---
    
    # Sostituisci "or 0.00" con "or Decimal('0.00')"
    entrate_correnti = Transazione.objects.filter(tipo='ENTRATA').aggregate(Sum('importo'))['importo__sum'] or Decimal('0.00') # <--- MODIFICATO
    uscite_correnti = Transazione.objects.filter(tipo='USCITA').aggregate(Sum('importo'))['importo__sum'] or Decimal('0.00') # <--- MODIFICATO
    
    # Questa riga ora funziona perché sono entrambi Decimal
    guadagno_corrente = entrate_correnti - uscite_correnti

    # --- 2. Calcolo dei Dati Annuali (RiepilogoMensile) ---
    riepiloghi = RiepilogoMensile.objects.all().order_by('-id')

    # Aggregazione per i totali e la media
    totali_annuali = RiepilogoMensile.objects.aggregate(
        guadagno_totale=Sum('guadagno_netto'),
        media_mensile=Avg('guadagno_netto')
    )

    # Anche qui, gestiamo il None con Decimal('0.00') per sicurezza
    guadagno_totale_annuale = totali_annuali['guadagno_totale'] or Decimal('0.00') # <--- MODIFICATO
    media_guadagno_mensile = totali_annuali['media_mensile'] or Decimal('0.00')   # <--- MODIFICATO
    
    context = {
        # ... il resto del context è identico
        'entrate_correnti': entrate_correnti,
        'uscite_correnti': uscite_correnti,
        'guadagno_corrente': guadagno_corrente,
        
        'riepiloghi': riepiloghi,
        
        'guadagno_totale_annuale': guadagno_totale_annuale,
        'media_guadagno_mensile': media_guadagno_mensile,
    }

    return render(request, 'finanze/riepilogo.html', context)