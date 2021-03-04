srpm:
	@echo "Hello?"
	spectool -g -R "$(spec)"
	rpmbuild -bs "$(spec)"
	cp *.srpm "$(outdir)"

.PHONY: srpm
