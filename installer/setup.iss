#define AppVersion GetEnv("APP_VERSION")
#define InputDir   GetEnv("INPUT_DIR")
#define OutputDirA GetEnv("OUTPUT_DIR")
#define Appexe     "Elite Dangerous Materials Trader"

#pragma message "AppVersion = {#AppVersion}"
#pragma message "InputDir   = {#InputDir}"
#pragma message "OutputDirA = {#OutputDirA}"
#pragma message "AppExe     = {#AppExe}"

[Setup]
AppName=Elite Dangerous Materials Trader
AppVersion={#AppVersion}
AppId={{865da89f-68b7-4f9a-9351-0a88ee05c4f7}}
WizardStyle=modern
DefaultDirName={autopf}\EDMT
DefaultGroupName=YuiYukihira
OutputDir={#OutputDirA}
OutputBaseFilename=EDMT-Setup-{#AppVersion}
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible
CloseApplications=yes
RestartApplications=no

[Files]
Source: "{#InputDir}\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"
Name: "startmenuicon"; Description: "Create a &Start Menu shortcut"; GroupDescription: "Additional shortcuts:"
Name: "quicklaunchicon"; Description: "Create a &Quick Launch shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\{#AppExe}"; Description: "Launch EDMT"; Flags: nowait postinstall skipifsilent