"""Render the supplied coordinates; not an application screenshot or simulation.

Optional dependencies: gemmi, numpy, matplotlib.
Run: python examples/materials/render_preview.py
"""
from pathlib import Path
import numpy as np
import gemmi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
PANELS = [
    ('Co3O4_COD_9005887.cif', 'Bulk crystal', '56 atoms: Co24 O32'),
    ('co3o4_112_surface_2x1x1.cif', '(112) surface supercell', '672 atoms: Co288 O384'),
    ('Co3O4_112_toluene_physisorption.cif', 'Toluene above the surface', '679 explicit atoms; H not shown'),
]
COLORS = {'Co': '#326bb3', 'O': '#dc6858', 'C': '#242c38'}
fig = plt.figure(figsize=(14, 5), facecolor='white')
for i, (filename, title, detail) in enumerate(PANELS, 1):
    block = gemmi.cif.read_file(str(HERE / 'files' / filename)).sole_block()
    xyz = np.array([[float(v) for v in block.find_values('_atom_site.Cartn_' + axis)]
                    for axis in 'xyz']).T
    elements = np.array(list(block.find_values('_atom_site.type_symbol')))
    ax = fig.add_subplot(1, 3, i, projection='3d')
    for element, color in COLORS.items():
        points = xyz[elements == element]
        if len(points):
            ax.scatter(*points.T, s=30 if element != 'C' else 42,
                       c=color, edgecolors='white', linewidths=.25, depthshade=True)
    mid = (xyz.min(axis=0) + xyz.max(axis=0)) / 2
    radius = max(np.ptp(xyz, axis=0)) * .55
    ax.set_xlim(mid[0]-radius, mid[0]+radius)
    ax.set_ylim(mid[1]-radius, mid[1]+radius)
    ax.set_zlim(mid[2]-radius, mid[2]+radius)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=20, azim=-65)
    ax.set_axis_off()
    ax.set_title(title, fontsize=14, fontweight='bold', color='#20304a', pad=2)
    ax.text2D(.5, -.02, detail, transform=ax.transAxes, ha='center', fontsize=10)
legend = [Line2D([0], [0], marker='o', color='none', markerfacecolor=c,
                 markeredgecolor='none', label=e, markersize=8) for e,c in COLORS.items()]
fig.legend(handles=legend, loc='lower center', ncol=3, frameon=False, bbox_to_anchor=(.5,.05))
fig.text(.5,.025,'Saved-coordinate previews | Independent panel scales | Initial geometry, not a relaxed adsorption state',
         ha='center', fontsize=10, color='#596477')
fig.subplots_adjust(left=.02,right=.98,bottom=.16,top=.9,wspace=.02)
fig.savefig(HERE / 'structure-preview.png', dpi=150)
plt.close(fig)
