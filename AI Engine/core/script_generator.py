class ScriptGenerator:
    """
    Translates abstract actions into executable PowerShell script blocks.
    """
    
    def generate_scripts(self, decision_plan: dict) -> list:
        """
        Takes a decision plan and returns a list of executable script objects.
        """
        scripts = []
        actions = decision_plan.get("actions", [])
        
        for i, action in enumerate(actions):
            script_content = ""
            action_type = action.get("type")
            
            if action_type == "tweak_power_plan":
                # Generate Power Plan Script
                script_content = """
# Set Power Plan to High Performance
$p = Get-CimInstance -Namespace root\\cimv2\\power -ClassName Win32_PowerPlan -Filter "ElementName='High performance'"
if ($p) {
    Invoke-CimMethod -InputObject $p -MethodName Activate
    Write-Output "Switched to High Performance."
} else {
    Write-Output "High Performance plan not found. Skipping."
}
"""
            elif action_type == "clear_temp_files":
                 script_content = """
# Clear Temp Files
$tempPath = $env:TEMP
if (Test-Path $tempPath) {
    Get-ChildItem -Path $tempPath -Recurse -Force -ErrorAction SilentlyContinue | 
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
    Write-Output "Cleaned Temp folder."
}
"""
            
            if script_content:
                scripts.append({
                    "id": f"action_{i}_{action_type}",
                    "description": action.get("type"),
                    "risk": action.get("risk"),
                    "content": script_content.strip()
                })
                
        return scripts
