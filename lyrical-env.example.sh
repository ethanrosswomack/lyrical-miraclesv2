# Copy this file to lyrical-env.sh and fill in the values before running
# scripts/publish_cloudflare.sh. All variables can also be exported manually or
# provided via CI secrets.

export WRANGLER_BIN="wrangler"          # path to wrangler CLI
export CF_ACCOUNT_ID=""                 # Cloudflare account ID
export CF_API_TOKEN=""                 # API token with R2 + D1 + Workers perms

export CF_R2_BUCKET="lyrical-miracles" # R2 bucket name
export CF_R2_AUDIO_PREFIX="audio"      # optional key prefix for audio assets
export CF_R2_IMAGE_PREFIX="images"     # optional key prefix for image assets

export CF_D1_DATABASE="lyrical_miracles"  # D1 database name (wrangler identifier)
export CF_D1_BINDING="LYRICAL_DB"         # Worker binding name for D1 (optional)

export CF_WORKER_NAME="lyrical-miracles-api" # Workers script name
export CF_VECTORIZE_INDEX="lyrical-miracles"  # Vectorize index (future use)
