from bing_image_downloader import downloader

downloader.download("car", limit=300,
                    output_dir='downloaded_images',
                    adult_filter_off=False,
                    force_replace=False,
                    timeout=60,
                    verbose=True)
