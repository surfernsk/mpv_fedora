Name:           mpv
Version:        0.35.1
Release:        3%{?dist}
Epoch:          1
Summary:        Movie player playing most video formats and DVDs
License:        GPLv2+ and LGPLv2+
URL:            http://%{name}.io/

Source0:        https://github.com/%{name}-player/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-config.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  luajit-devel
BuildRequires:  perl(Encode)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  waf

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  libshaderc-devel
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(vapoursynth) >= 24
BuildRequires:  pkgconfig(vapoursynth-script) >= 23
%else
BuildRequires:  python2-docutils
%endif

BuildRequires:  pkgconfig(alsa) >= 1.0.18
BuildRequires:  pkgconfig(caca) >= 0.99.beta18
BuildRequires:  pkgconfig(dvdnav) >= 4.2.0
BuildRequires:  pkgconfig(dvdread) >= 4.1.0
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(ffnvcodec) >= 8.1.24.1
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libavcodec) >= 58.16.100
BuildRequires:  pkgconfig(libavdevice) >= 58.0.0
BuildRequires:  pkgconfig(libavfilter) >= 7.14.100
BuildRequires:  pkgconfig(libavformat) >= 58.9.100
BuildRequires:  pkgconfig(libavutil) >= 56.12.100
BuildRequires:  pkgconfig(libass) >= 0.12.1
BuildRequires:  pkgconfig(libbluray) >= 0.3.0
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libswresample) >= 3.0.100
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 0.36.0
BuildRequires:  pkgconfig(libva-drm) >= 0.36.0
BuildRequires:  pkgconfig(libva-x11) >= 0.36.0
BuildRequires:  pkgconfig(libva-wayland) >= 0.36.0
BuildRequires:  pkgconfig(openal) >= 1.13
BuildRequires:  pkgconfig(rubberband) >= 1.8.0
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vdpau) >= 0.2
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client) >= 1.6.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.6.0
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11) >= 1.0.0
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xinerama) >= 1.0.0
BuildRequires:  pkgconfig(xpresent) >= 1.0.0
BuildRequires:  pkgconfig(xfixes) >= 6.0.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.3.0
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
BuildRequires:  pkgconfig(xscrnsaver) >= 1.0.0
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zimg) >= 2.9
BuildRequires:  pkgconfig(libarchive)	>= 3.4.0

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libplacebo) >= 1.18.0
BuildRequires:  pkgconfig(mujs) >= 1.0.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
%endif

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires:       hicolor-icon-theme

Provides:       mplayer-backend

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%package        libs
Summary:        Dynamic library for Mpv frontends
Provides:       libmpv = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      libmpv < %{?epoch:%{epoch}:}%{version}-%{release}

%description    libs
This package contains the dynamic library libmpv, which provides access to Mpv.

%package        libs-devel
Summary:        Development package for libmpv
Requires:       mpv-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libmpv-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      libmpv-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig

%description    libs-devel
Libmpv development header files and libraries.


%package zsh
Summary:        zsh completion functions for MPV
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       zsh

%description zsh
zsh completion functions for MPV.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -I%{_includedir}/cuda"
export CCFLAGS="%{optflags} -I%{_includedir}/cuda"
waf configure \
    --bindir=%{_bindir} \
    --confdir=%{_sysconfdir}/%{name} \
    --disable-build-date \
    --docdir=%{_docdir}/%{name} \
    --enable-cdda \
    --enable-cplugins \
    --enable-dvbin \
    --enable-dvdnav \
    --enable-drm \
    --enable-libarchive \
    --enable-libmpv-shared \
    --enable-vaapi \
    --enable-vaapi-drm \
    --enable-html-build \
    --enable-openal \
    --enable-sdl2 \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix}

waf build %{?_smp_mflags}

%install
waf install --destdir=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 644 README.md etc/input.conf etc/mpv.conf -t %{buildroot}%{_docdir}/%{name}

%post
%if 0%{?rhel} == 7
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
%endif

%postun
%if 0%{?rhel} == 7
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
%endif

%ldconfig_scriptlets libs

%files
%license LICENSE.* Copyright RELEASE_NOTES
%{_metainfodir}/%{name}.metainfo.xml
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/bash-completion/completions/mpv
%_datadir/zsh/site-functions/*
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/encoding-profiles.conf

%files libs
%license LICENSE.* Copyright RELEASE_NOTES
%{_libdir}/libmpv.so.*

%files libs-devel
%{_includedir}/%{name}
%{_libdir}/libmpv.so
%{_libdir}/pkgconfig/mpv.pc

%files zsh
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Jan 31 2023 Evgeny Lensky <surfernsk@gmail.com> - 1:0.35.1-3
- bump to 0.35.1

* Tue Jan 31 2023 Evgeny Lensky <surfernsk@gmail.com> - 1:0.35.1-1
- bump to 0.35.1

* Wed Nov 23 2022 Evgeny Lensky <surfernsk@gmail.com> - 1:0.35.0-2
- fix x11 (update x11 BuildRequires)

* Wed Nov 23 2022 Evgeny Lensky <surfernsk@gmail.com> - 1:0.35.0-1
- bump to 0.35.0

* Fri Jan 14 2022 Evgeny Lensky <surfernsk@gmail.com> - 1:0.34.1-1
- bump to 0.34.1

* Tue Nov 02 2021 Evgeny Lensky <surfernsk@gmail.com> - 1:0.34.0-1
- Update to 0.34.0

* Mon Apr 05 2021 Evgeny Lensky <surfernsk@gmail.com> - 1:0.33.1-1
- Update to 0.33.1

* Mon Nov 23 2020 Evgeny Lensky <surfernsk@gmail.com> - 1:0.33.0-1
- Update to 0.33.0

* Sun Feb 09 2020 Evgeny Lensky <surfernsk@gmail.com> - 1:0.32.1-1
- some fix on .spec (upd from negativo17)

* Sun Feb 09 2020 Evgeny Lensky <surfernsk@gmail.com> - 1:0.32.0-1
- Update to 0.32.0 (fadora 31 only)

* Sat Jan 04 2020 Evgeny Lensky <surfernsk@gmail.com> - 1:0.31.0-1
- Update to 0.31.0

* Sun Oct 27 2019 Evgeny Lensky <surfernsk@gmail.com> - 1:0.30.0-1
- Update to 0.30.0

* Tue Oct 22 2019 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-7
- Rebuild for updated dependencies.

* Tue Sep 03 2019 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-6
- Rebuild for FFMpeg update.

* Sun Mar 24 2019 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-5
- Rebuild for FFMpeg update.

* Tue Feb 19 2019 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-4
- Rebuild for ffmpeg update.

* Tue Nov 13 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-3
- Rebuild for FFMpeg update.

* Wed Oct 31 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-2
- Add libshaderc dependency for Vulkan support with NVidia 410 drivers (thanks
  Jens Peters).

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.1-1
- Update to 0.29.1.

* Fri Sep 28 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.0-3
- Disable PDF doc generation, it is not supported on RHEL and does not yet work
  with Python 3 (Fedora 29+).

* Thu Sep 27 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.0-2
- Add GCC build requirement.

* Tue Jul 24 2018 Simone Caronni <negativo17@gmail.com> - 1:0.29.0-1
- Update to 0.29.0.
- Update SPEC file.

* Thu May 17 2018 Simone Caronni <negativo17@gmail.com> - 1:0.28.2-3
- Enable Vulkan also on RHEL/CentOS.

* Sun May 13 2018 Simone Caronni <negativo17@gmail.com> - 1:0.28.2-2
- Enable Vulkan support (thanks Jens Peters).
- Enable Wayland support (thanks Jens Peters).

* Thu Apr 26 2018 Simone Caronni <negativo17@gmail.com> - 1:0.28.2-1
- Update to 0.28.2.
- Update SPEC file.

* Wed Apr 11 2018 Simone Caronni <negativo17@gmail.com> - 1:0.27.2-1
- Update to 0.27.2.

* Thu Oct 26 2017 Simone Caronni <negativo17@gmail.com> - 1:0.27.0-1
- Update to 0.27.0.

* Tue Oct 03 2017 Simone Caronni <negativo17@gmail.com> - 1:0.26.0-2
- Enable DVB support that had been disabled by default in mpv 0.26 (thanks Jens
  Peters).
- Sort build requirements.

* Tue Sep 12 2017 Simone Caronni <negativo17@gmail.com> - 1:0.26.0-1
- Update to 0.26.0.

* Thu Jun 08 2017 Simone Caronni <negativo17@gmail.com> - 1:0.25.0-2
- Enable C plugins.

* Thu Jun 01 2017 Simone Caronni <negativo17@gmail.com> - 1:0.25.0-1
- Update to 0.25.0.
- Adjust epoch requirements.
- Require at least FFmpeg 3.3 to build, for dynamic CUDA loading.

* Thu Mar 23 2017 Simone Caronni <negativo17@gmail.com> - 1:0.24.0-2
- Rebuild for libbluray update.

* Tue Feb 14 2017 Simone Caronni <negativo17@gmail.com> - 1:0.24.0-1
- Update to 0.24.0.
- Disable CUDA support until FFmpeg 3.4, it does not work without the new
  dynamic CUDA library loading introduced in FFmpeg 3.4.

* Tue Jan 03 2017 Simone Caronni <negativo17@gmail.com> - 1:0.23.0-1
- Update to 0.23.0.
- Bump up FFmpeg build requirements to pull in newest FFmpeg at build time.

* Tue Nov 29 2016 Simone Caronni <negativo17@gmail.com> - 1:0.22.0-3
- Patch so minimal updates to FFmpeg will not require a rebuild

* Tue Nov 29 2016 Simone Caronni <negativo17@gmail.com> - 1:0.22.0-2
- MPV triggers a warning even if the sahred object major version to which it is
  linked against is the same. Rebuild for FFMpeg 3.2.1.

* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 1:0.22.0-1
- Update to 0.22.0.

* Fri Nov 11 2016 Simone Caronni <negativo17@gmail.com> - 1:0.21.0-1
- Update to 0.21.0, enable CUDA support for x86_64.

* Wed Sep 14 2016 Simone Caronni <negativo17@gmail.com> - 1:0.20.0-2
- Adjust Lua build requirements.

* Sat Aug 27 2016 Simone Caronni <negativo17@gmail.com> - 1:0.20.0-1
- Update to 0.20.0, update build requirements.
- Enable building on CentOS/RHEL 7.
- Enable PDF/HTML docs.
- Enable libarchive, OpenAL, Colour Ascii Art (caca) support.
- Do not run update-desktop-database on Fedora 25+ as per packaging guidelines.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:0.19.0-1
- Update to 0.19.0, bump Epoch.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.18.1-2
- Rebuilt for ffmpeg-3.1.1

* Tue Jul 26 2016 Miro Hrončok <mhroncok@redhat.com> - 0.18.1-1
- Update to 0.18.1
- Remove patch for Fedora < 22

* Sun Jul 03 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-3
- BRs in alphabetical order, rename of sub-packages libs and other improvements

* Thu Jun 30 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-2
- Add BR perl(Encode) to build on F24 (merge from Adrian Reber PR)

* Tue Jun 28 2016 Sérgio Basto <sergio@serjux.com> - 0.18.0-1
- Update to 0.18.0
