import time
import os

def join():
	start = time.time()
	img_path = '../datasets/all_images'
	cap_path = '../datasets/all_captions'
	save_dir = '../datasets'
	out_path = '../datasets/ddmd.token.txt'
	error = []
	ignore = 'Readme.txt'
	data = ''
	for img_idx, imgfile_name in enumerate(os.listdir(img_path)):
		img_name = imgfile_name.split('.')[0]
		for cap_idx, capfile_name in enumerate(os.listdir(cap_path)):
			cap_name = capfile_name.split('.')[0]
			if not ignore in capfile_name:
				if cap_name == img_name:
					print('{}--->{}'.format(capfile_name, imgfile_name))
					try:
						caption_file = os.path.join(cap_path, capfile_name)
						with open(caption_file, 'r') as reader:
							for cap_line in reader:
								if (cap_line != '\n'):
									data = data + imgfile_name + '\t' + cap_line + '\n'
					except:
						error.append('{}\t{}'.format(cap_path, capfile_name))
						print('Error: {} ============================================'.format(capfile_name))
						continue
		with open(out_path, 'w') as writer:
			writer.write(data)
			writer.write('\n')

	with open('../datasets/error_pdf2txt.txt', 'w') as out_error:
		out_error.write('\n'.join(error))
	print('Running Time: {} seconds'.format(time.time() - start))

if __name__ == "__main__":
	join()