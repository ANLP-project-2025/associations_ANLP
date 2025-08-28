import pandas as pd
import numpy as np
import random


def process(file_path: str, output_path: str = None, seed: int = 42) -> None:
    # Set global seed for reproducibility
    np.random.seed(seed)
    random.seed(seed)

    # Load CSV
    df = pd.read_csv(file_path)

    # Lowercase cue and response columns
    for col in ["cue", "R1", "R2", "R3"]:
        df[col] = df[col].str.lower()

    # Original stats
    original_row_count = len(df)
    original_unique_cues = df["cue"].nunique()

    # Drop rows with any missing R1/R2/R3
    cleaned_df = df.dropna(subset=["R1", "R2", "R3"])
    new_row_count = len(cleaned_df)
    new_unique_cues = cleaned_df["cue"].nunique()





    # Unique responses across R1–R3
    unique_responses = pd.unique(cleaned_df[["R1", "R2", "R3"]].values.ravel())
    num_unique_responses = len(unique_responses)

    # Stats on cue frequencies
    cue_counts = cleaned_df["cue"].value_counts()
    min_per_cue = cue_counts.min()
    max_per_cue = cue_counts.max()
    mean_per_cue = cue_counts.mean()
    median_per_cue = cue_counts.median()

    # Percentage of rows removed
    percent_removed = 100 * (original_row_count - new_row_count) / original_row_count

    # Print main stats
    print(f"✅ Cleaned data saved to: {output_path}")
    print(f"Original number of different cues: {original_unique_cues}")
    print(f"New number of different cues: {new_unique_cues}")
    print(f"Original number of rows: {original_row_count}")
    print(f"New number of rows: {new_row_count}")
    print(f"Percentage of rows removed: {percent_removed:.2f}%")
    print(f"Number of different responses (R1, R2, R3): {num_unique_responses}")
    print(f"Rows per cue - min: {min_per_cue}, max: {max_per_cue}, mean: {mean_per_cue:.2f}, median: {median_per_cue}")

    # Print cue frequency thresholds
    print("\n📊 Cues with at least N rows:")
    for threshold in range(10, 101, 10):
        count = (cue_counts >= threshold).sum()
        print(f" ≥ {threshold}: {count} cues")

    # ── Filter to cues with at least 80 rows ───────────────────────────────
    valid_cues = cue_counts[cue_counts >= 80].index
    filtered_df = cleaned_df[cleaned_df["cue"].isin(valid_cues)]

    # ── Sample exactly 80 rows per cue ─────────────────────────────────────
    sampled_df = (
        filtered_df.groupby("cue", group_keys=False)
        .sample(n=80, random_state=seed)  # ✅ reproducible sampling
        .reset_index(drop=True)
    )
    sampled_df = sampled_df.map(lambda x: str(x).lower() if not pd.isna(x) else x)


    sampled_df.to_excel(output_path, index=False)

    print(f"\n✅ Downsampled dataset (80 rows per cue) saved to: {output_path}")

    # Downsampled stats
    downsampled_row_count = len(sampled_df)
    downsampled_unique_cues = sampled_df["cue"].nunique()
    downsampled_unique_responses = pd.unique(sampled_df[["R1", "R2", "R3"]].values.ravel())
    num_downsampled_unique_responses = len(downsampled_unique_responses)
    downsampled_cue_counts = sampled_df["cue"].value_counts()
    min_down = downsampled_cue_counts.min()
    max_down = downsampled_cue_counts.max()
    mean_down = downsampled_cue_counts.mean()
    median_down = downsampled_cue_counts.median()

    # Print downsampled stats
    print(f"Downsampled number of different cues: {downsampled_unique_cues}")
    print(f"Downsampled number of rows: {downsampled_row_count}")
    print(f"Number of different responses (R1, R2, R3): {num_downsampled_unique_responses}")
    print(f"Rows per cue - min: {min_down}, max: {max_down}, mean: {mean_down:.2f}, median: {median_down}")




process(r"J:\ANLP code\anlp_project\data\processed SWOW100 from LWOW code\FA_Humans.csv",
            r"J:\ANLP code\anlp_project\data\final data\cleaned_data_FA_Humans.xlsx