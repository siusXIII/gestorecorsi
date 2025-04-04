import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None


    def handlePrintCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            # self._view.lvTxtOut.controls.append(
            #     ft.Text("Attenzione, selezionare un periodo didattico!", color="red"))
            self._view.create_alert("Attenzione, selezionare un periodo didattico!")
            self._view.update_page()
            return

        #a questo punto pd="I" oppure pd="II"
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPD = self._model.getCorsiPD(pdInt)
        if len(corsiPD) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato per questo periodo!"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} periodo didattico."))
        for c in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(c))
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Seleziona il periodo didattico!")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPDwithI = self._model.getCorsiPDwithIscritti(pdInt)
        if len(corsiPDwithI) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato per questo periodo!"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Dettagli corsi del {pd} periodo didattico."))
        for c in corsiPDwithI:
            self._view.lvTxtOut.controls.append(ft.Text(f"{c[0]} - Numero iscritti: {c[1]}"))
        self._view.update_page()


    def handlePrintIscrittiCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Seleziona il corso!")
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Studenti iscritti al corso: {self._ddCodinsValue}"))
        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)
        if len(studenti) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessuno studente iscritto a questo corso!"))
            self._view.update_page()
            return
        for s in studenti:
            self._view.lvTxtOut.controls.append(ft.Text(s))
        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Seleziona il corso!")
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"CDS che frequentano il corso: {self._ddCodinsValue}"))
        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun cds offre questo corso!"))
            self._view.update_page()
            return
        for c in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"{c[0]} - Numero iscritti: {c[1]}"))
        self._view.update_page()


    def fillddCodins(self):
        # for cod in self._model.getCodins():
        #     self._view.ddCodins.options.append(ft.dropdown.Option(cod))

        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins,
                                                                  data = c,
                                                                  on_click=self._choiceDDCodins))

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)
        print("In _choiceDDCodins", type(self._ddCodinsValue))
    def ddCodinsSelected(self, e):
        print("In ddCodinsSelected", type(self._view.ddCodins.value))