indir=$1

python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x-duc.yaml \
            --checkpoint pretrained_models/fast_421_res50-shuffle_256x192.pth \
            --indir $indir \
            --outdir $indir

