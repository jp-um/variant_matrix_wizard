from vmw.ui.wizardpages.vm_wizard_page import VMWizardPage


class Step0DataFilesTypeSelection(VMWizardPage):

    def __init__(self, parent):
        super().__init__(parent, "Select your type of data files")
