srpm:
	@echo "Hello?"
	spectool -g -R "$(spec)"
	rpmbuild -bs "$(spec)"
	cp *.rpm "$(outdir)"

.PHONY: srpm
