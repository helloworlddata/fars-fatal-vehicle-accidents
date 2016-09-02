#!/usr/bin/env sh
# usage: ./scripts/fetch_and_unpack_mirror SRCURL DESTPATH

# Download from zipped mirror file (SRCURL), save to DESTPATH,
# unpack to dirname DESTPATH

src_url="$1"
dest_path="$2"
dest_dir=$(dirname $dest_path)

ZIP_SUBDIR='ftp.nhtsa.dot.gov--fars-master/fars' # the relevant subdirectory in the zip file
(>&2 echo "...")

if ! [ -f "$dest_path" ]; then
  (>&2 echo "Downloading from: \t$src_url")
  (>&2 echo "Saving to: \t$dest_path")

  curl -L "$src_url" -o "$dest_path"
else

  (>&2 echo "$dest_path already exists. Delete it manually if you want to re-download it...")
  sleep 2
fi


(>&2 echo '...')


better_dest_path="$dest_dir/fars"
if [[ -e "$better_dest_path" ]]; then
  # move fars/* to $dest_path/fars
  (>&2 echo "Error: $better_dest_path exists. Unzipping canceled.")
  (>&2 echo "Manually remove the directory:")
  (>&2 echo $better_dest_path)
  (>&2 echo "...Then rerun this script.")
else
  (>&2 echo "Unzipping $dest_path into $dest_dir")
  sleep 2
  unzip "$dest_path" \
      "$ZIP_SUBDIR/*"   \
      -d  "$dest_dir"
  mv "$dest_dir/$ZIP_SUBDIR" "$better_dest_path"
fi
