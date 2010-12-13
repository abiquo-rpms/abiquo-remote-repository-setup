================================
  Abiquo OVF Index Generator 0.1
================================

Run the scripts to generate the ovfindex.xml from an absolute file system path:
  
    - In Windows:
        generateindex.bat c:\path\to\ovfs http://export.location.com/ myApplianceRepository
        
    - In Unix-like:
        chmod u+x generateindex.sh            
        ./generateindex.sh /path/to/ovfs http://export.location.com/ myApplianceRepository
    
    - Or just invoke java directly:
        java -jar lib/indexgenerator-0.1.jar /path/to/ovfs http://export.location.com/ myApplianceRepository

