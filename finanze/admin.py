# finanze/admin.py

from django.contrib import admin
from .models import Transazione, RiepilogoMensile

# Registra la Transazione normalmente (non hai bisogno di personalizzazione qui)
admin.site.register(Transazione)

# ELIMINA la riga "admin.site.register(RiepilogoMensile)" che causava l'errore

# Personalizza la visualizzazione del RiepilogoMensile e registrala
@admin.register(RiepilogoMensile)
class RiepilogoMensileAdmin(admin.ModelAdmin):
    # Campi da visualizzare nella lista (Read)
    list_display = ('mese', 'totale_entrate', 'totale_uscite', 'guadagno_netto')
    
    # Campi che appaiono nel modulo di Aggiunta/Modifica (Create/Update)
    # Perfetto, nasconde guadagno_netto e mostra solo i dati inseriti.
    fields = ('mese', 'totale_entrate', 'totale_uscite') 
    
    # Rendi il guadagno in sola lettura (Buona pratica, anche se 'fields' lo nasconde)
    readonly_fields = ('guadagno_netto',)