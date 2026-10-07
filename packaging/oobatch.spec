Name:           oobatch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Non-interactive batch job manager queueing tasks when system load factor drops.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobatch
Source0:        oobatch-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobatch is a sovereign, capability-bounded BATCH QUEUE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobatch
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobatch-uninstall

%files
/usr/bin/oobatch
/usr/bin/oobatch-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
