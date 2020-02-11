param([Parameter(Mandatory = $true,ValueFromPipeline = $true)]
	[string]
	$action, [switch]$Elevated)


function Test-Admin {
  $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
  $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated)
    {
        # tried to elevate, did not work, aborting
    }
    else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated -action "{1}"' -f ($myinvocation.MyCommand.Definition,$action))
}

exit

}

'running with full privileges'


if ($action -like 'activate')  {
(Get-Content C:\Windows\System32\drivers\etc\hosts -Raw) -replace '#+10.3.4.53','10.3.4.53' | Set-Content -Path C:\Windows\System32\drivers\etc\hosts
Sleep 2
echo $action
}elseif($action -like 'deactivate'){

(Get-Content C:\Windows\System32\drivers\etc\hosts -Raw) -replace '10.3.4.53','#10.3.4.53' | Set-Content -Path C:\Windows\System32\drivers\etc\hosts
Sleep 2
echo $action
}

Sleep 2

Stop-Process -Name "powershell"