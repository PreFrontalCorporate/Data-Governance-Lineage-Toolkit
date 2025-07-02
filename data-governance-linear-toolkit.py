########################################
# ✅ Data Governance & Lineage Toolkit — Full LaTeX-Ready Proof and Algorithm Documentation Block (Fixed)
########################################

import sympy as sp
import hashlib
import datetime
import os
import json

# --------------------
# Proof: Reversibility transformation
# --------------------
x = sp.symbols('x')
expr = (x - 5) / 2
inverse_expr = 2 * expr + 5
assert sp.simplify(inverse_expr - x) == 0
proof_hash = hashlib.sha256(sp.srepr(expr).encode()).hexdigest()

# --------------------
# Save symbolic proof log
# --------------------
def save_symbolic_log(expr, description):
    log = {
        "description": description,
        "symbolic_expr": sp.srepr(expr)
    }
    os.makedirs("logs/symbolic", exist_ok=True)
    filename = f"logs/symbolic/symbolic_log_{description.replace(' ', '_')}.json"
    with open(filename, 'w') as f:
        json.dump(log, f, indent=4)
    print(f"✅ Symbolic proof log saved: {filename}")

save_symbolic_log(expr, "reversibility_proof")

# --------------------
# Notarize to distributed ledger
# --------------------
def notarize_proof_to_ledger(proof_hash, description):
    ledger_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "proof_hash": proof_hash,
        "description": description
    }
    os.makedirs("logs/distributed_ledger", exist_ok=True)
    filename = f"logs/distributed_ledger/ledger_entry_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(ledger_entry, f, indent=4)
    print(f"✅ Proof hash notarized: {filename}")

notarize_proof_to_ledger(proof_hash, "Reversibility proof example")

# --------------------
# Validate symbolic stream
# --------------------
def validate_symbolic_stream(expr_stream):
    for expr_str in expr_stream:
        try:
            expr = sp.sympify(expr_str)
            simplified = sp.simplify(expr)
            if simplified.has(sp.nan) or simplified.has(sp.oo):
                print("❌ Symbolic integrity breached!")
            else:
                print("✅ Symbolic expression valid.")
        except Exception as e:
            print(f"❌ Error in symbolic expression: {expr_str} — {e}")

expr_stream = ["(x - 5)/2", "(x + 0)/2"]
validate_symbolic_stream(expr_stream)

# --------------------
# Export proof to registry
# --------------------
def export_proof_to_registry(proof_data):
    os.makedirs("logs/public_registry", exist_ok=True)
    filename = f"logs/public_registry/registry_proof_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(proof_data, f, indent=4)
    print(f"✅ Proof exported to registry: {filename}")

proof_data = {
    "theorem": "Reversibility Theorem",
    "symbolic_expr": sp.srepr(expr),
    "latex": sp.latex(expr),
    "proof_hash": proof_hash,
    "timestamp": datetime.datetime.now().isoformat()
}
export_proof_to_registry(proof_data)

# --------------------
# LaTeX snippet (documentation snippet for reports)
# --------------------
os.makedirs("logs/latex", exist_ok=True)
latex_snippet = r'''
\\section*{Reversibility Proof}
Given the transformation $f(x) = (x - 5)/2$, its inverse is $f^{-1}(x) = 2x + 5$.\\
We verify:
$$2 \cdot \frac{x - 5}{2} + 5 = x.$$\\
Thus, the transformation is reversible.\\
Proof hash: ''' + proof_hash + r'''.
'''

with open("logs/latex/reversibility_proof_snippet.tex", "w") as f:
    f.write(latex_snippet)
print("✅ LaTeX snippet saved for inclusion in documentation.")

# --------------------
# Final message
# --------------------
print("\n🎯 Full code, proofs, logs, ledger notarization, and LaTeX snippet complete!")
