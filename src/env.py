settings = {
  'wifiAP': 'RSA_Device',
  'wifiPassword': 'WeLoveRSA',
  'controllerName': 'grow-controller', # Used for DHCP hostname
  'logInclude': ['.*'], # regex supported
  'logExclude': [], # regex supported
  'httpTimeout': 2, # seconds

  # Auto-Updating
  'githubRemote': '',
  'githubUsername': '', # Optional: Without this, you may hit API limits
  'githubToken': '', # Optional: Without this, you may hit API limits0
  'githubRemoteBranch': "master"
}
