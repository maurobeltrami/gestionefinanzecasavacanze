# finanze/models.py

from django.db import models
from django.utils import timezone

# Scelta del tipo di transazione
TIPO_SCELTE = [
    ('ENTRATA', 'Entrata'),
    ('USCITA', 'Uscita'),
]

# Tabella 1: Transazioni (solo per il mese corrente)
class Transazione(models.Model):
    # La colonna ID è creata automaticamente da Django
    
    tipo = models.CharField(
        max_length=7,
        choices=TIPO_SCELTE,
        default='ENTRATA',
    )
    importo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    # Colonna opzionale che potresti usare per filtrare/ordinare
    data_creazione = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.tipo}: {self.importo} €"

# Tabella 2: Riepilogo Mensile (Archivio annuale)
class RiepilogoMensile(models.Model):
    # La colonna ID è creata automaticamente
    
    mese = models.CharField(max_length=20, unique=True)
    totale_entrate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    totale_uscite = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Campo che verrà calcolato
    guadagno_netto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False) 

    class Meta:
        verbose_name_plural = "Riepiloghi Mensili"

    # QUESTO È IL CODICE AGGIUNTO O MODIFICATO:
    def save(self, *args, **kwargs):
        """Calcola il guadagno netto prima di salvare il record."""
        self.guadagno_netto = self.totale_entrate - self.totale_uscite
        super().save(*args, **kwargs) # Esegui il salvataggio normale

    def __str__(self):
        return self.mese