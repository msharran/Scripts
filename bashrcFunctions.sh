function work(){
	echo "‹‹ Workspace ››"
	cd /Users/KINGSLAYER/Documents/workspace;
	ls -l;
}
export work

function restart_postgres(){
	brew services stop postgresql;
	rm /usr/local/var/postgres/postmaster.pid;
	brew services start postgresql;
}
export restart_postgres

function stop_postgres(){
	brew services stop postgresql;
	rm /usr/local/var/postgres/postmaster.pid;
	brew services start postgresql;
}
export stop_postgres

function start_postgres(){
	brew services start postgresql;
}
export start_postgres

# oh-my-zsh theme
ZSH_THEME="sunrise"
