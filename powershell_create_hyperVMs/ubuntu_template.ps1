######################################################
###              Template Definition               ###
######################################################
$VM = "{0:d2}" -f ((Get-VM -name VM-WEB-*).length + 1)
# VM Name
$VMName          = "VM-WEB-$VM"

# Automatic Start Action (Nothing = 0, Start =1, StartifRunning = 2)
$AutoStartAction = 1
# In second
$AutoStartDelay  = 10
# Automatic Start Action (TurnOff = 0, Save =1, Shutdown = 2)
$AutoStopAction  = 2


###### Hardware Configuration ######
# VM Path
$VMPath         = "G:\VHDS"

# VM Generation (1 or 2)
$Gen            = 1

# Processor Number
$ProcessorCount = 1

## Memory (Static = 0 or Dynamic = 1)
$Memory         = 1
# StaticMemory
$StaticMemory   = 8GB

# DynamicMemory
$StartupMemory  = 2GB
$MinMemory      = 1GB
$MaxMemory      = 8GB

# Sysprep VHD path (The VHD will be copied to the VM folder)
$SysVHDPath     = "D:\VHDS\VM-templates\VM-WEB-Ubuntu1804.vhdx"
# Rename the VHD copied in VM folder to:
$OsDiskName     = $VMName

### Network Adapters
# Primary Network interface: VMSwitch 
$VMSwitchName = "VirtualSwitch-#4"
$VlanId       = 0
$VMQ          = $False
$IPSecOffload = $False
$SRIOV        = $False
$MacSpoofing  = $False
$DHCPGuard    = $False
$RouterGuard  = $False
$NicTeaming   = $False



######################################################
###           VM Creation and Configuration        ###
######################################################

## Creation of the VM
# Creation without VHD and with a default memory value (will be changed after)
New-VM -Name $VMName `
       -Path $VMPath `
       -NoVHD `
       -Generation $Gen `
       -MemoryStartupBytes 1GB `
       -SwitchName $VMSwitchName


if ($AutoStartAction -eq 0){$StartAction = "Nothing"}
Elseif ($AutoStartAction -eq 1){$StartAction = "Start"}
Else{$StartAction = "StartIfRunning"}

if ($AutoStopAction -eq 0){$StopAction = "TurnOff"}
Elseif ($AutoStopAction -eq 1){$StopAction = "Save"}
Else{$StopAction = "Shutdown"}

## Changing the number of processor and the memory
# If Static Memory
if (!$Memory){
    
    Set-VM -Name $VMName `
           -ProcessorCount $ProcessorCount `
           -StaticMemory `
           -MemoryStartupBytes $StaticMemory `
           -AutomaticStartAction $StartAction `
           -AutomaticStartDelay $AutoStartDelay `
           -AutomaticStopAction $StopAction


}
# If Dynamic Memory
Else{
    Set-VM -Name $VMName `
           -ProcessorCount $ProcessorCount `
           -DynamicMemory `
           -MemoryMinimumBytes $MinMemory `
           -MemoryStartupBytes $StartupMemory `
           -MemoryMaximumBytes $MaxMemory `
           -AutomaticStartAction $StartAction `
           -AutomaticStartDelay $AutoStartDelay `
           -AutomaticStopAction $StopAction

}

## Set the primary network adapters
$PrimaryNetAdapter = Get-VM $VMName | Get-VMNetworkAdapter
if ($VlanId -gt 0){$PrimaryNetAdapter | Set-VMNetworkAdapterVLAN -Access -VlanId $VlanId}
else{$PrimaryNetAdapter | Set-VMNetworkAdapterVLAN -untagged}

## VHD(X) OS disk copy
$OsDiskInfo = Get-Item $SysVHDPath
Copy-Item -Path $SysVHDPath -Destination $($VMPath + "\" + $VMName)
Rename-Item -Path $($VMPath + "\" + $VMName + "\" + $OsDiskInfo.Name) -NewName $($OsDiskName + $OsDiskInfo.Extension)

# Attach the VHD(x) to the VM
Add-VMHardDiskDrive -VMName $VMName -Path $($VMPath + "\" + $VMName + "\" + $OsDiskName + $OsDiskInfo.Extension)

$OsVirtualDrive = Get-VMHardDiskDrive -VMName $VMName -ControllerNumber 0
     
# Change the boot order to the VHDX first
Set-VMFirmware -VMName $VMName -FirstBootDevice $OsVirtualDrive

