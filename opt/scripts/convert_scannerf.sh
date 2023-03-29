# TRAIN_JSON="train_all_500.json"
VAL_JSON="val_all.json"
TEST_JSON="test_all.json"
SCANNERF_DIR="/home/ccl/Datasets/NeRF/ScanNerf"

for SUFFIX in all_25_random all_50_random; do
  TRAIN_JSON="train_$SUFFIX.json"
  OUT_DIR="/home/ccl/Datasets/NeRF/ScanNerf-NSVF/$SUFFIX"
  for SCENE_PATH in $SCANNERF_DIR/*; do
    SCENE=`basename $SCENE_PATH`
    echo $SCENE
    python scannerf2nsvf.py "$SCANNERF_DIR/$SCENE" "$OUT_DIR/$SCENE" --train_json=$TRAIN_JSON --val_json=$VAL_JSON --test_json=$TEST_JSON
  done
done