import os
import tarfile
from datetime import datetime

source_dir = "/home/control/devops-toolkit"
backup_file = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"

with tarfile.open(backup_file, "w:gz") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))

print(f"Backup created: {backup_file}")
 
