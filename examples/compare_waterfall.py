import os
from epr_svd_tool import (
    load_bruker_kinetic,
    prepare_kinetic_matrix,
    save_comparison_waterfall,
)

def main():
    files = [f for f in os.listdir(".") if f.endswith(".DSC")]

    outdir = "Figures"
    os.makedirs(outdir, exist_ok=True)

    rank = 3
    poly_order = 1
    every = 1

    for filename in files:
        field, matrix, par = load_bruker_kinetic(filename)
        raw_matrix, svd_matrix, difference, s = prepare_kinetic_matrix(
            field,
            matrix,
            poly_order=poly_order,
            rank=rank,
        )

        title = str(par.get("TITL", filename))
        outpath = os.path.join(outdir, f"{title}_compare_waterfall_rank{rank}.png")

        save_comparison_waterfall(
            field,
            raw_matrix,
            svd_matrix,
            outpath,
            title=title,
            every=every,
        )

        print(f"Saved: {outpath}")
        print("First 10 singular values:", s[:10])

if __name__ == "__main__":
    main()