TRAIN_JSON="train_all_100.json"
VAL_JSON="val_all.json"
TEST_JSON="test_all.json"
SCANNERF_DIR="/home/ccl/Datasets/NeRF/ScanNerf"
OUT_DIR="/home/ccl/Datasets/NeRF/ScanNerf-NSVF/all_100"
SCENES=`ls $SCANNERF_DIR`

for SCENE_PATH in $SCANNERF_DIR/*; do
  SCENE=`basename $SCENE_PATH`
  echo $SCENE
  python scannerf2nsvf.py "$SCANNERF_DIR/$SCENE" "$OUT_DIR/$SCENE" --train_json=$TRAIN_JSON --val_json=$VAL_JSON --test_json=$TEST_JSON
done