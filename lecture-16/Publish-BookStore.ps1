Compress-Archive -Path $home\source\repos\nrw-intro-to-python\lecture-16\PyBookStore\* -DestinationPath ./pyBookStore.zip
$uri = (Publish-AzWebApp -ArchivePath .\pyBookStore.zip -Force -ResourceGroupName RediPython -Name PyBookStore).HostNames[0]
Write-Host ('{0}/Books' -f $uri)
