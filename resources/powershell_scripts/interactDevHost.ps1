param([Parameter(Mandatory = $true,ValueFromPipeline = $true)]
	[string]
	$action, [switch]$Elevated)


function Test-Admin {
  $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
  $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

function Replace-Hosts([string]$FilePath, [string]$Pattern, [string]$Replacement){
[System.IO.File]::WriteAllText(
$FilePath,
        ([System.IO.File]::ReadAllText($FilePath) -replace $Pattern, $Replacement))
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
$FilePath='C:\Windows\System32\drivers\etc\hosts'


if ($action -like 'activate')  {
 $Pattern='#+10.3.4.53'
 $Replacement='10.3.4.53'
 echo $action

    Replace-Hosts $FilePath $Pattern $Replacement
    }

elseif($action -like 'deactivate'){
 $Pattern='10.3.4.53'
 $Replacement='#10.3.4.53'
 echo $action

Replace-Hosts $FilePath $Pattern $Replacement
}

Sleep 2

Stop-Process -Name "powershell"