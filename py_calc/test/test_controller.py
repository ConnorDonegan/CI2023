def test_calculateResult(controller):
    controller._view.setDisplayText("3+3")
    controller._calculateResult()
    assert controller._view.displayText() == "6"

def test_returnSignal(controller):
    """Tests the Return key binding interface to our Qt display widget."""
    from PyQt5 import QtCore, QtGui

    controller._view.setDisplayText("1+2")
    event = QtGui.QKeyEvent(
        QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
    )
    controller._view.display.keyPressEvent(event)
    controller._calculateResult()
    print("The result is:", controller._view.displayText())
    assert controller._view.displayText() == "3"
