## About the connector
JS code snippet integration for FortiSOAR allows you to seamlessly incorporate JavaScript code snippets into your playbooks. With this integration, you can harness the power of JavaScript to enhance your automation and response workflows, enabling greater flexibility and customization.
<p>This document provides information about the JS Code Snippet Connector, which facilitates automated interactions, with a JS Code Snippet server using FortiSOAR&trade; playbooks. Add the JS Code Snippet Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with JS Code Snippet.</p>
### Version information

Connector Version: 1.0.0


Authored By: Fortinet CSE

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-jscode-snippet`

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>JS Code Snippet</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Allow Imports<br></td><td>Specify whether you want to allow JSNode imports or not. By default it is set to False.<br>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Execute JavaScript Code<br></td><td>Execute JavaScript Code as part of your Playbooks<br></td><td>run_js_code <br/><br></td></tr>
</tbody></table>
### operation: Execute JavaScript Code
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>JavaScript Code<br></td><td>Specify the JS code which needs to be executed.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "code_output": {}
</code><code><br>}</code>
## Included playbooks
The `Sample - jscode-snippet - 1.0.0` playbook collection comes bundled with the JS Code Snippet connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the JS Code Snippet connector.

- Sample 1 > Run JS Code
- Sample 2 > Run JS Code

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
