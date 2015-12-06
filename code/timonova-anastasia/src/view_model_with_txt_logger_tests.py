from view_model.tests_for_viewmodel import TestForViewModel
from txt_logger import TxtLogger


class TestForViewModelWithTxtLogger(TestForViewModel):

    def SetUpWithTxtLogger(self):
        self.real_logger = TxtLogger("./ViewModelWithTxtLoggerTests.log")



# package ru.unn.agile.ComplexNumber.infrastructure_lab3_legacy;
#
# import ru.unn.agile.ComplexNumber.viewmodel_lab3_legacy.ViewModel;
# import ru.unn.agile.ComplexNumber.viewmodel_lab3_legacy.ViewModelTests;
#
# public class ViewModelWithTxtLoggerTests extends ViewModelTests {
#     @Override
#     public void setUp() {
#         TxtLogger realLogger =
#             new TxtLogger("./ViewModelWithTxtLoggerTests-lab3-legacy.log");
#         super.setViewModel(new ViewModel(realLogger));
#     }
# }
