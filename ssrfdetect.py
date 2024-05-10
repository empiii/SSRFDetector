from burp import IBurpExtender, IHttpListener, ITab
from javax.swing import JPanel, JLabel, JTextArea, JScrollPane
from java.awt import BorderLayout

class BurpExtender(IBurpExtender, IHttpListener, ITab):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Create UI
        self._panel = JPanel(BorderLayout())
        self._panel.add(JLabel("Potential Parameter vulneable, Check vuln SSRF e Path Traversal. Execute PoC with BurpCollaborator."), BorderLayout.NORTH)
        self._output = JTextArea()
        scrollPane = JScrollPane(self._output)
        self._panel.add(scrollPane, BorderLayout.CENTER)
        
        # Register the listener
        callbacks.registerHttpListener(self)
        
        # Add the custom tab to Burp's UI
        callbacks.addSuiteTab(self)
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if not messageIsRequest:
            return

        request = messageInfo.getRequest()
        analyzedRequest = self._helpers.analyzeRequest(request)
        method = analyzedRequest.getMethod()
        if method != "POST":
            return

        body = request[analyzedRequest.getBodyOffset():].tostring()
        parameters = body.split("&")
        
        for param in parameters:
            if "=" in param:
                name, value = param.split("=")
                try:
                    decoded_value = self._helpers.urlDecode(value)
                except:
                    decoded_value = value
                if decoded_value.startswith("http"):
                    self._output.append("Found parameter with request http value: " + name + "=" + decoded_value + "\n")
                    self._output.setCaretPosition(self._output.getDocument().getLength())
    
    def getTabCaption(self):
        return "SSRF Detector"
    
    def getUiComponent(self):
        return self._panel
