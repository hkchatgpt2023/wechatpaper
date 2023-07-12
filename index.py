#!-*- coding:utf-8 -*-
import os

def main():
	word_docs = []
	doc_folders = []
	rootdir = os.getcwd()
	print(rootdir)
	with open('file_list.md', 'w') as f:
		for file in os.listdir(rootdir):
			print(file)
		# for subdir, dirs, files in os.walk(rootdir):
		# 	print(dirs)
		# 	for file in files:
		# 		if file.endswith(",docx") or file.endswith(".doc"):
		# 			print(file)
		# 			# 将匹配到的Word文档添加到列表中，同时保留该文档所在的目录路径。
		# 			word_path = os.path.join(subdir, file)
		# 			word_docs.append(word_path)
		#
		# 		# 为每个单独存在于目录结构层级中的唯一相对路径创建一个保存List.
		# 		folder_rel_path = os.path.relpath(subdir, rootdir)
		# 		if folder_rel_path not in doc_folders:
		# 			doc_folders.append(folder_rel_path)
		# print(word_docs)
		# # 将所有路径转换成Markdown链接格式，包括每个相对路径或 "folder"
		# md_links_and_folders = [f"- [{os.path.basename(path)}]({path}) (in `{folder}`)"
		# 						for path in word_docs
		# 						for folder in [next(
		# 		(f for f in doc_folders if f == os.path.relpath(os.path.dirname(path), rootdir)), 'Folder Not Found')]]
		# # 在文件中写入每个Markdown链接，以换行符分隔它们。
		# print(md_links_and_folders)
		# f.write('\n'.join(md_links_and_folders))
		# print("okay")

if __name__ == '__main__':
	main()