indir=$1

python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml \
            --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth \
            --indir $indir \
            --outdir $indir
