#!/usr/bin/env python3
from pathlib import Path
import sys


fair = Path(sys.argv[1])
source = fair.read_text()
needle = "\tutil_est_dequeue(&rq->cfs, p);\n"
bore = """#ifdef CONFIG_SCHED_BORE
\tif (task_sleep) {
\t\tcfs_rq = cfs_rq_of(se);
\t\tif (cfs_rq->curr == se)
\t\t\tupdate_curr(cfs_rq);
\t\trestart_burst(se);
\t}
#endif
"""

if source.count(needle) != 1:
    raise SystemExit("Expected exactly one util_est_dequeue insertion point")

fair.write_text(source.replace(needle, needle + bore, 1))
