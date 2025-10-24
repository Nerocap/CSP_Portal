# Architektur der Lineareinheit-Steuerung

## Überblick
Das Programm steuert eine Lineareinheit über eine serielle Schnittstelle.
Die Steuerung erfolgt über eine GUI mit PyQt6.  
Die Software ist in drei Hauptschichten unterteilt:

1. **GUI (View)**  
   - Stellt die Benutzeroberfläche bereit (Buttons, Eingabefelder, Statusanzeigen).
   - Realisiert mit PyQt6.
   - Sendet Benutzeraktionen an den Controller.

2. **Controller (Logic)**  
   - Vermittelt zwischen GUI und Hardware.
   - Übersetzt Benutzeraktionen in Bewegungsbefehle.
   - Hält den aktuellen Zustand der Lineareinheit (z. B. Position).

3. **Hardware (Driver / Model)**  
   - Enthält die Schnittstellen zur Lineareinheit.
   - Realisiert durch `pyserial` (Kommunikation über COM-Port).
   - Bietet Funktionen wie `fahren()`, `stoppen()`, `referenzfahrt()`.

---

## Modulübersicht

