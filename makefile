SHELL=/bin/bash
CONDAROOT = /home/guillermo/anaconda3/etc/profile.d/conda.sh
 
all:
	echo "make install <- Main installation (conda, block main commits, ... )"
	echo "check_old_branches <- Check branches that are already merged in main."
	echo "refresh_main_and_clean_old_branches <- Delete branches and switch to main."
	

	echo "run make -s .......................to surpress nafty raw echo commands"

install:
	# sign
	git config user.name "CryptoCashCashoo"
	git config user.email cryptocashcashoo@gmail.com

	# BLOCK COMMITS TO MAIN 
	cp installation/pre-commit.sh .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

	# INSTALL CONDA
	source $(CONDAROOT)
	conda env remove -p $(CURDIR)/conda | true 
	rm -rf $(CURDIR)/conda | true
	mkdir $(CURDIR)/conda
	conda env create --prefix="./conda" -f "installation/env.yml" 
	source $(CONDAROOT) && conda activate $(CURDIR)/conda && conda env export | grep -v "^prefix: " > $(CURDIR)/installation/fixed-env.yml
	echo "Installed and saved in installation/fixed-env! "
	echo "conda activate ./conda"

check_old_branches:
	git fetch --prune
	git checkout -q main && git pull
	git checkout -q main && git for-each-ref refs/heads/ "--format=%(refname:short)" | while read branch; do mergeBase=$$(git merge-base main $$branch) && [[ $$(git cherry main $$(git commit-tree $$(git rev-parse $$branch^{tree}) -p $$mergeBase -m _)) == "-"* ]] && echo "$$branch is merged into main and can be deleted";  done

refresh_main_and_clean_old_branches:
	git fetch --prune
	git checkout -q main && git pull
	git checkout -q main && git for-each-ref refs/heads/ "--format=%(refname:short)" | while read branch; do mergeBase=$$(git merge-base main $$branch) && [[ $$(git cherry main $$(git commit-tree $$(git rev-parse $$branch^{tree}) -p $$mergeBase -m _)) == "-"* ]] && git branch -D $$branch; done
	
