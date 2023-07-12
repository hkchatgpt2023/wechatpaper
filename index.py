#!-*- coding:utf-8 -*-
import os
from loguru import  logger

def get_files(rootdir):
	word_docs = []
	if os.path.isdir(rootdir):
		logger.info(rootdir)
		for p in os.listdir(rootdir):
			if os.path.isdir(os.path.join(rootdir,p)):
				w= get_files(os.path.join(rootdir,p))
				if w:
					word_docs.extend(w)
			else:
				if p.endswith(".docx") or p.endswith(".doc"):
					word_path = os.path.join(rootdir, p)
					word_docs.append(word_path)
	return word_docs


def main():
	rootdir = "./"
	logger.info(rootdir)
	if os.path.isdir(rootdir):
		for p in os.listdir(rootdir):
			if os.path.isdir(os.path.join(rootdir,p)) and not p.startswith("."):
				logger.info(p)
				file_name = p+"_数据列表.md"
				with open(file_name, "w") as f:
					word_docs = get_files(os.path.join(rootdir,p))
					md_links = [f"- [{os.path.basename(path)}]({os.path.dirname(path)})" for path in word_docs]
					f.write('\n'.join(md_links))



if __name__ == '__main__':
	main()