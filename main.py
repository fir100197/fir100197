a

    FÁaY ã                   @   sŠ  d dl Z d dlZd dlZd dlZd dlmZmZmZ ejdd d dlmZmZ d dlZd dl	Z	eƒ  ej
ZejZ
ejZejZejZejZe
eeeegZdd„ Zeƒ  dd	„ Zed
ƒ edƒ edƒ ed
ƒ e j d¡sèeedƒƒZneddƒZe  ¡ Zdd„ Z!dd„ Z"dd„ Z#dd„ Z$dd„ Z%dd„ Z&dd„ Z'dd „ Z(d!d"„ Z)d#d$„ Z*d%d&„ Z+d'd(„ Z,d)d*„ Z-d+d,„ Z.d-d.„ Z/d/d0„ Z0d1d2„ Z1d3d4„ Z2d5d6„ Z3d7d8„ Z4d9d:„ Z5d;d<„ Z6e7d=kr†e j d>¡sÌe  8d>¡ e j d?¡säed?d@ƒ e j d¡seddAƒZ9e9 :e¡ e9 ;¡  dBZ<e	 =dCei¡Z>dDdEdFœZ?ej@dGe<e?e>dHZAeA 	¡ ZBzøeBdI eeƒkr<eCejDej dJ ƒ eCejDejE dK ƒ eCejDejE dL ƒ eCejDejE dM ƒ eCejDejE dN ƒ eCejDejE dO ƒ eCejDejE dP ƒ eCejDejE dQ ƒ eCejDejE dR ƒ eCejDejE dS ƒ eCejDejE dT ƒ eCejDejE dU ƒ eCejDej dV ƒ eCejDejE dW ƒ eCejDejE dX ƒ eCejDejE dY ƒ eCejDejE dZ ƒ eCejDejE d[ ƒ eCejDej d\ ƒ eCejDejE d] ƒ eCejDejE d^ ƒ eCejDejE d_ ƒ eCejDej d` ƒ eCejDejE da ƒ eCejDejE db ƒ eCejDejE dc ƒ d dlFZFg dd¢ZGeGD ] ZHeCeF Ie¡› eH› e› ƒ qveJedeƒƒZKeKdfkr¸e!ƒ  n„eKdgkrÌe"ƒ  npeKdhkràe#ƒ  n\eKdikrôe$ƒ  nHeKdjkre%ƒ  n4eKdkkre&ƒ  n eKdlkr0e'ƒ  neKdmkrBe(ƒ  núeKdnkrTe/ƒ  nèeKdokrfe0ƒ  nÖeKdpkrxe6ƒ  nÄeKdqkrŠe)ƒ  n²eKdrkrœe*ƒ  n eKdskr®e+ƒ  nŽeKdtkrÀe-ƒ  n|eKdukrÒe.ƒ  njeKdvkräe1ƒ  nXeKdwkröe2ƒ  nFeKdxkre3ƒ  n4eKdykre4ƒ  n"eKdzkr,e5ƒ  neKd{kr<eLƒ  W nF   d dlFZFg d|¢ZGeGD ] ZHeCeF Ie¡› eH› e› ƒ qZeL Y n0 dS )}é    N©ÚForeÚBackÚStyleT©Z	autoreset©Úinitr   c                  C   s8   dd l } g d¢}|D ]}t|  t¡› |› t› ƒ qd S )Nr   ©z- _____     _                _                z-|_   _|__ | |__   __ _     / \   _ __  _ __  z-  | |/ _ \| |_ \ / _` |   / _ \ | |_ \| |_ \ z-  | | (_) | | | | (_| |  / ___ \| |_) | |_) |z-  |_|\___/|_| |_|\__,_| /_/   \_\ .__/| .__/ z-                                |_|   |_|    )ÚrandomÚprintÚchoiceÚcolorsÚn©r
   ÚlegendÚdev© r   úmain.pyÚ
legend_dev   s    	r   c                 C   s.   | D ]$}t j |¡ t j ¡  t d¡ qd S )Ng{®Gáz”?)ÚsysÚstdoutÚwriteÚflushÚtimeÚsleep)Úmessager   r   r   r   ÚLEGEND_DEVty%   s    
r   ú;========================= Main Developer  : T.me/Tohaputra
z9========================= Buy Tools  WA : T.me/Tohaputra
ú
Loading.....
ú=--------------------------------------------------------100%
zlicence.txtz
Enter your LICENCE KEY : Úrc                  C   sD  ddl m}  ddlm} dd l}ddlm} dd l}dd l}ddlm}m	}m
} tƒ  |jdd t
dd	ƒŒ}	d
d„ | |	¡D ƒ}
d}|
D ]Z}| |¡}
|d7 }t|j|j d
|
›  ƒ | d|
› ddƒ}| |
¡ | ¡  tƒ  qŠd}W d   ƒ n1 sþ0    Y  t|r |j|j d ndƒ t|j|j d ƒ tƒ  d S )Nr   ©ÚTelegramClient©Úutils©Úreaderr   Tr   ú	phone.csvr    c                 S   s   g | ]}|d  ‘qS ©r   r   ©Ú.0Úrowr   r   r   Ú
<listcomp>D   ó    zlogin1.<locals>.<listcomp>é   úLogin ú	sessions/é‚$ Ú 7e14b38d250953c8c1e94fd7b2d63550zAll Number Login Done !úError!zPress Enter to Exit)Ú
telethon.syncr"   Útelethonr$   Úcsvr&   ÚconfigparserÚcoloramar   r   r   Úlegend_devpostr   ÚopenÚparse_phoner   ÚBRIGHTÚGREENÚstartÚ
disconnectÚRESETÚYELLOWÚinput)r"   r$   r6   r&   r7   r8   r   r   r   ÚfÚstr_listÚpoÚpphoneÚphoneÚclientÚdoner   r   r   Úlogin16   s0    

"rJ   c               
   C   s  dd l } ddl m}m}m} | jdd tƒ  ddlm} ddlm	} ddl
m} dd l}dd l
}tdƒ}	td	ƒ}
g }d
}tddƒN}
d
d„ | |
¡D ƒ}d}|D ]´}|d7 }| |¡}td|› ƒ |d|› |	|
ƒ}| ¡  | ¡ sRz*tdƒ t|ƒ}t|ƒ}| |¡ W q¤W n: |yP   tdƒ t|ƒ}t|ƒ}| |¡ Y q¤Y n0 tƒ  q¤d}tdƒ t|ddiŽ tdƒ tdddd*}|j|ddd}| |¡ W d   ƒ n1 s¼0    Y  W d   ƒ n1 sÜ0    Y  dd„ }d d!„ }|ƒ  |ƒ  t|rd"nd#ƒ d S )$Nr   r   Tr   r!   r#   )ÚPhoneNumberBannedErrorr1   r2   Fr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   e   r-   zbanfilter.<locals>.<listcomp>r.   r/   r0   zThis Phone Has Been RevokedZBanzList Of Banned NumbersÚsepÚ
zSaved In BanNumers.csvúBanNumbers.csvÚwúUTF-8©Úencodingú,©Z	delimiterÚlineterminatorc               	   S   s|  dd l } dd l}g }g }g }g }g }tddƒ$}|D ]}| |¡ q4W d   ƒ n1 sX0    Y  |D ]}	t|	ƒ dd¡}
| |
¡ qftdƒV}tddƒ,}|D ]}| | d	d¡¡ q W d   ƒ n1 sÌ0    Y  W d   ƒ n1 sê0    Y  tddƒ&}|D ]}| |¡ qW d   ƒ n1 s,0    Y  |D ] }
t|
ƒ dd¡}| |¡ q:t|ƒ}t|ƒ}| |¡}|D ]}	|	|vrz| |	¡ qztd
ddd(}| j	|dd
}| 
|¡ W d   ƒ n1 sÔ0    Y  td
ƒb}tddƒ6}|D ] }t|ƒ dd¡}| |¡ qøW d   ƒ n1 s00    Y  W d   ƒ n1 sP0    Y  | d¡ | d
d¡ t
dƒ d S )Nr   r'   r    rM   Ú rN   zoutfile.csvrO   rS   ú	unban.csvrP   rQ   ©rU   z(Done,All Banned Number Have Been Removed)r6   Úosr:   ÚappendÚstrÚreplacer   ÚsetÚintersectionÚwriterÚ	writerowsÚremoveÚrenamer   )r6   rY   Ú
collectionÚncÚcollection1Únc1ÚmaindÚinfileÚlineÚxÚmod_xÚoutfileÚline1ÚiÚmod_iÚuniqueÚunique1ÚitdÚ	writeFiler_   ÚlastÚfinalÚline3r   r   r   Ú
autoremove   sL    *P.

*N
zbanfilter.<locals>.autoremovec               	   S   s    dd l } dd l}tdƒV}tddƒ,}|D ]}| | dd¡¡ q*W d   ƒ n1 sV0    Y  W d   ƒ n1 st0    Y  | d¡ | dd¡ tdƒ d S )Nr   r'   rW   rO   rS   rV   Zcomplete)r6   rY   r:   r   r\   ra   rb   r   ©r6   rY   rh   rl   ri   r   r   r   ÚdellstÂ   s    P
zbanfilter.<locals>.dellstúDone!r3   )r8   r   r   r   r   r9   r4   r"   r5   r$   Útelethon.errors.rpcerrorlistrK   r6   r7   Úintr[   r:   r&   r;   r   ÚconnectÚis_user_authorizedrZ   r_   r`   rB   )r8   r   r   r   r"   r$   rK   r6   r7   Úapi_idÚapi_hashÚMadeByRexhacksrI   rC   rD   rE   Zunparsed_phonerG   rH   ÚrexhacksÚNero_oprs   r_   rw   ry   r   r   r   Ú	banfilterS   s`    




J5r„   c            !   
      sÔ  dd l } ddl m‰ m}m‰ | jdd tƒ  ddlm} ddlm} ddlm	}m
} ddlm} ddlm
} dd l}dd l}dd	lm}	 dd l}
dd l } ddl m‰ m}m‰ | jdd dd l}dd l}dd l}dd l}
d
}d}g }d}d}td
dƒ8}dd„ | |¡D ƒ}d}|D ]ô}| |¡}|d7 }tˆjˆ j dˆj› dˆjˆ j › d|›  ƒ |d|› ddƒ}| |¡ ||jjddƒ | |d¡ |  d¡ | !|¡}|D ]}t|j"ƒ q°t#|ƒ}||v rÞ|d7 }ntdƒ t#|ƒ}| $|¡ | %¡  tƒ  d}qtdƒ t|ddiŽ W d   ƒ n1 s:0    Y  t|› dƒ tdd d!d"*}|j&|d#dd$}| '|¡ W d   ƒ n1 s’0    Y  ‡ ‡fd%d&„}d'd(„ } |ƒ  | ƒ  t(|rÊd)nd*ƒ d S )+Nr   r   Tr   r!   ©Ú	functionsÚtypesr#   )ÚYouBlockedUserErrorr%   ZSpamBotZbirdFr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   ï   r-   zspambotch.<locals>.<listcomp>r.   r/   ú r0   r1   r2   z@SpamBot©Úidz/startzyou are limitedzList Of limited NumbersrL   rM   z - Accounts Are Usableúlegend1.csvrO   rP   rQ   rS   rT   c               	      s°  dd l } dd l}g }g }g }g }g }tddƒ$}|D ]}| |¡ q4W d   ƒ n1 sX0    Y  |D ]}	t|	ƒ dd¡}
| |
¡ qftˆjˆ j d ƒ t	ƒ }tdƒ\}t|› dd	ƒ,}|D ]}| 
| d
d¡¡ qÀW d   ƒ n1 sì0    Y  W d   ƒ n1 s0    Y  t|› ddƒ&}|D ]}
| |
¡ q,W d   ƒ n1 sT0    Y  |D ] }t|ƒ dd¡}| |¡ qbt|ƒ}t|ƒ}| |¡}|D ]}	|	|vr¢| |	¡ q¢tdd	dd
(}| j
|dd}| |¡ W d   ƒ n1 sü0    Y  tdƒb}tdd	ƒ6}|D ] }t|ƒ dd¡}| 
|¡ q W d   ƒ n1 sX0    Y  W d   ƒ n1 sx0    Y  | d¡ | dd¡ tˆjˆ j d ƒ d S )Nr   r'   r    rM   rV   zAEnter The File Name Where You Want To Save Your Limited Numbers :rŒ   z.csvrO   rS   úlegend2.csvrP   rQ   rX   zTask Completed!!!!!!)r6   rY   r:   rZ   r[   r\   r   r<   r=   rB   r   r]   r^   r_   r`   ra   rb   ÚRED)r6   rY   rc   rd   re   rf   rg   rh   ri   rj   rk   Zrexfilerl   rm   rn   ro   rp   rq   rr   rs   r_   rt   ru   rv   ©r   r   r   r   Ú	forremove  sP    *R.

*N
zspambotch.<locals>.forremovec               	   S   s¢   dd l } dd l}tdƒV}tddƒ,}|D ]}| | dd¡¡ q*W d   ƒ n1 sV0    Y  W d   ƒ n1 st0    Y  | d¡ | dd¡ | d¡ d S )Nr   r'   r   rO   rS   rV   rŒ   )r6   rY   r:   r   r\   ra   rb   rx   r   r   r   Ú
deletelist8  s    P
zspambotch.<locals>.deletelistrz   r3   ))r8   r   r   r   r   r9   r4   r"   r5   r†   r‡   r$   r{   rˆ   r6   r   r&   r7   Ú
subprocessÚrequestsrY   r:   r;   r   r<   r=   Ú	RESET_ALLr@   r>   ÚcontactsZUnblockRequestÚsend_messager   Zget_messagesr   r[   rZ   r?   r_   r`   rB   )!r8   r   r"   r†   r‡   r$   rˆ   r6   r   r&   r7   r’   r“   rY   Zbotr‚   r   r    rI   rC   rD   rE   rF   rG   rH   Úmsgr   Ú
Legend_devrƒ   rs   r_   r   r‘   r   r   r   Ú	spambotchÔ   sr     
0





.**r™   c            1         s   ddl m}  dd l‰ dd l}dd l}dd l}ddlm} ddlm	}m
}m}m}m
}	m}
m} ddlm}m}
 dd l}ddlm}m}m} |jdd tƒ  dd l}dd l}dd l}| ¡ }| d	¡ |d
 d  ¡ }| d¡}d
}d}|d
 d  ¡ }|j|j d t!|j"|j# d|›  ƒ z
| d|› ||ƒ}| $¡  | %¡ rt!|j"|j& d ƒ d}| '¡ }||
dd }||
dd }t(dddd} ˆ j)| ddd}!|! *g d¢¡ z"|D ]}"z| +|"¡ W n& t,yð }# zW Y d }#~#n
d }#~#0 0 t!|j"|j- d|"› d  ƒ g }$|j.|"dd!}$|$D ]¦}%|%j/r8|%j/}&nd"}&|%j0rL|%j0}'nd#}'t1|%j2|ƒrd|}(n:t1|%j2|ƒrv|}(t1|%j2|	ƒrˆ|}(t1|%j2|ƒrž|%j2j3}(|( 4d$¡})|! *||&|%j5|'|"|)g¡ |d }q$q¶W n& t,yø }# zW Y d }#~#n
d }#~#0 0 |  6¡  t!d%|ƒ nt!|j"|j7 d&|›  ƒ W n: t,yd }# z t!|j"|j7 d' ƒ W Y d }#~#n
d }#~#0 0 t8ƒ }*‡ fd(d)„}+‡ fd*d+„},|+ƒ  |,ƒ  t(d,d-ddª}-ˆ  9|-¡}.t(ddddp} ˆ j)| ddd}!|! *g d¢¡ d}/|.D ]8}0|/d7 }/|! *|/|0d |0d. |0d/ |0d0 |0d1 f¡ qàW d   ƒ n1 s00    Y  W d   ƒ n1 sP0    Y  | :d2¡ | :d,¡ t!|j"|j& d3 ƒ t!|j"|j# d4 ƒ t;ƒ  d S )5Nr   r!   )ÚJoinChannelRequest©ÚInputPeerEmptyÚUserStatusOfflineÚUserStatusRecentlyÚUserStatusLastMonthÚUserStatusLastWeekÚPeerUserÚPeerChannel©ÚdatetimeÚ	timedeltar   Tr   ú
config.inir˜   Ú	FromGrouprS   r1   r2   ÚPhoneNumber©Úlevelú
Logging For r0   ú
login Doner.   éùÿÿÿ©Zdayséâÿÿÿúdata.csvrO   rP   rQ   rM   rT   ©zsr. no.Úusernamezuser idÚnameÚgroupZStatuszScrabing Members from ú group.....©Z
aggressiverV   ZRexhacksú%Y%m%dzCount : úlogin fail z
login failc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S ©Nr°   r    rP   rQ   rV   ú1.csvrO   rS   rM   rT   ©Úlistr:   r&   rZ   ra   r_   r`   ©ÚlinesZreadFiler&   r+   Zfieldrs   r_   ©r6   r   r   Úmainš  s    

,zscraper1.<locals>.mainc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S ©Nrº   r    rP   rQ   r²   ú2.csvrO   rS   rM   rT   r»   r½   r¿   r   r   Úmain1®  s    

,zscraper1.<locals>.main1rÂ   r    é   é   é   é   rº   zTask completedúEnter any key to exit)<r4   r"   r6   r7   Úloggingr5   Útelethon.tl.functions.channelsrš   Útelethon.tl.typesrœ   r   rž   rŸ   r    r¡   r¢   r¤   r¥   r8   r   r   r   r   r9   r“   r   rY   ÚConfigParserÚreadÚstripÚsplitÚbasicConfigÚWARNINGr   r<   r@   r}   r~   r=   Únowr:   r_   ÚwriterowÚ
get_entityÚ	ExceptionrA   Úget_participantsr²   Ú
first_nameÚ
isinstanceÚstatusÚ
was_onlineÚstrftimer‹   ÚcloserŽ   r¼   r&   ra   rB   )1r"   r7   rÉ   r5   rš   rœ   r   rž   rŸ   r    r¡   r¢   r¤   r¥   r8   r   r   r   r“   r   rY   ÚconfigZlink1ÚlinksÚAPI_IDÚHashIDrG   rH   ÚcountÚtodayÚ	last_weekÚ
last_monthrC   r_   ÚlinkÚeÚall_participantsÚuserr²   r³   Údate_onlineÚdate_online_strr¾   rÀ   rÃ   ÚsourceÚrdrrn   r+   r   r¿   r   Úscraper1F  s®    $





*
n

rí   c                  C   sø   dd l } ddlm} ddlm} ddlm} |  ¡ }| d¡ d}d}|d d	  	¡ }|d
|› ||ƒ}| 
¡  | ¡ sØz0| |¡ | 
|tdƒ¡ tdƒ | 
|¡ W n. |yÖ   td
ƒ}	tdƒ |j
|	d Y n0 tdƒ}
|||
ƒƒ tdƒ d S )Nr   r!   ©ÚImportChatInviteRequest©ÚSessionPasswordNeededErrorr¦   r1   r2   r˜   r¨   r0   úEnter code: rV   úEnter password: ©ÚpasswordzEnter Private Group Hash : z Joined Group Sucessfully........)r7   r4   r"   Útelethon.tl.functions.messagesrï   Útelethon.errorsrñ   rÌ   rÍ   rÎ   r}   r~   Úsend_code_requestÚsign_inrB   r   )r7   r"   rï   rñ   rÝ   rß   rà   rG   rH   rõ   Zgplinkr   r   r   ÚprivategroupJoiner×  s0    

rú   c            %         sx  ddl m} m} dd l}dd l }ddl m} m} ddlm‰m‰ dd l‰dd l}ddl	m
} ddl	m}m‰m
‰m‰m‰m
}m} dd l}	dd l}
ddlm‰ m}m‰ |
jdd	 tƒ  dd l}dd l}
dd l}‡ ‡‡‡‡‡‡‡‡f	d
d„}tˆjˆ j d ƒ ttƒ ƒ}|}ˆ  ¡ ˆ| d
  !d¡}g }|	 "¡ }| #d¡ |d d  $¡ }| %d¡}d}d}|d d  $¡ }|j&|j'd tˆjˆ j( d|›  ƒ zd| d|› ||ƒ}| )¡  | *¡ rÞtˆjˆ j+ d ƒ ||||ƒ}ntˆjˆ j, |› d ƒ W nB t-y< } z(t|ƒ tˆjˆ j d ƒ W Y d }~n
d }~0 0 t.ƒ }‡fdd„}‡fdd„}|ƒ  |ƒ  t/d d!d"d#ª}ˆ 0|¡} t/d$d%d"d#p}!ˆj1|!dd&d'}"|" 2g d(¢¡ d}#| D ]8}$|#d)7 }#|" 2|#|$d) |$d* |$d+ |$d, |$d- f¡ q¸W d   ƒ n1 s0    Y  W d   ƒ n1 s(0    Y  | 3d.¡ | 3d ¡ tˆjˆ j+ d/ ƒ tˆjˆ j d0 ƒ tƒ  d S )1Nr   ©r"   Ú
connection©r"   Úsyncr£   ©r¡   r›   r   Tr   c                    sø  ˆ  ¡ }|ˆdd }|ˆdd }| d¡}g d¢g}d}|  ¡ }|D ]D}	tˆjˆ j d|	› d ƒ |  |	¡}
z| j|
jd	d
}W n0 t	y¸ } zW Y d }~qHW Y d }~n
d }~0 0 |D ]Î}
|
j
d kr¾z²t|
jˆƒrà|}n8t|
jˆƒrð|}t|
jˆƒr|}t|
jˆƒr|
jj
}| d¡}t|ƒt|ƒkr||t|
j
ƒt|
jƒt|
jd |
j ƒt|
jƒt|ƒg}| |¡ |d7 }W q¾   Y q¾0 q¾qH|rÜtdd
ddd$}ˆ |¡}| |¡ W d   ƒ n1 sÒ0    Y  td|ƒ |  ¡  tƒ  d S )Nr­   r®   r¯   r·   r±   r.   úFilter Members from rµ   Tr¶   r‰   r°   rO   úutf-8rV   ©rR   Únewlinez
Members : ©rÒ   rÛ   Zget_dialogsr   r<   r@   rÔ   rÖ   r‹   rÕ   r²   rØ   rÙ   rÚ   r[   r×   Ú	last_nameÚtitlerZ   r:   r_   r`   r?   ©rH   rå   Úlast_dayrâ   rã   rä   Úará   Zdialogsrn   r´   rç   ræ   rè   ré   rê   ÚbrC   r   ©	r   r   rŸ   r    r   rž   r6   r¤   r¥   r   r   Únfilter  sR    



"

$ÿ


*
zdailyfilter.<locals>.nfilterz
Enter the day for filter :r®   r·   r¦   r˜   r§   rS   r1   r2   r¨   r©   r«   r0   r¬   z login failzPlease Enter Vailed Groupc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S r¹   r»   r½   r¿   r   r   rÀ   Q  s    

,zdailyfilter.<locals>.mainc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S rÁ   r»   r½   r¿   r   r   rÃ   e  s    

,zdailyfilter.<locals>.main1rÂ   r    rP   rQ   r°   rO   rM   rT   r±   r.   rÄ   rÅ   rÆ   rÇ   rº   úFilter completedrÈ   ©4r5   r"   rü   rÉ   rþ   r¤   r¥   r6   ÚjsonrË   r¡   rœ   r   rž   rŸ   r    r¢   r7   r8   r   r   r   r   r9   r“   r   rY   r   r<   rA   r|   rB   rÒ   rÛ   rÌ   rÍ   rÎ   rÏ   rÐ   rÑ   r@   r}   r~   r=   rŽ   rÕ   r¼   r:   r&   r_   rÓ   ra   ©%r"   rü   rÉ   r5   rþ   r  r¡   rœ   r¢   r7   r8   r   r“   r   rY   r  r   r  ZdelerÝ   rÞ   rå   rß   rà   rG   rH   r	  ræ   r¾   rÀ   rÃ   rë   rì   rC   r_   rn   r+   r   r  r   Údailyfilterò  sr    $,



*
n

r  c            %         s|  ddl m} m} dd l}dd l }ddl m} m} ddlm‰m‰ dd l‰dd l}ddl	m
} ddl	m}m‰m
‰m‰m‰m
}m} dd l}	dd l}
ddlm‰ m}m‰ |
jdd	 tƒ  dd l}dd l}
dd l}‡ ‡‡‡‡‡‡‡‡f	d
d„}tˆjˆ j d ƒ ttƒ ƒ}|d
 }ˆ  ¡ ˆ| d  !d¡}g }|	 "¡ }| #d¡ |d d  $¡ }| %d¡}d}d}|d d  $¡ }|j&|j'd tˆjˆ j( d|›  ƒ zd| d|› ||ƒ}| )¡  | *¡ râtˆjˆ j+ d ƒ ||||ƒ}ntˆjˆ j, d|›  ƒ W nB t-y@ } z(t|ƒ tˆjˆ j d ƒ W Y d }~n
d }~0 0 t.ƒ }‡fdd„}‡fdd „}|ƒ  |ƒ  t/d!d"d#d$ª}ˆ 0|¡} t/d%d&d#d$p}!ˆj1|!dd'd(}"|" 2g d)¢¡ d}#| D ]8}$|#d*7 }#|" 2|#|$d* |$d+ |$d, |$d- |$d. f¡ q¼W d   ƒ n1 s0    Y  W d   ƒ n1 s,0    Y  | 3d/¡ | 3d!¡ tˆjˆ j+ d0 ƒ tˆjˆ j d1 ƒ tƒ  d S )2Nr   rû   rý   r£   rÿ   r›   r   Tr   c                    sø  ˆ  ¡ }|ˆdd }|ˆdd }| d¡}g d¢g}d}|  ¡ }|D ]D}	tˆjˆ j d|	› d ƒ |  |	¡}
z| j|
jd	d
}W n0 t	y¸ } zW Y d }~qHW Y d }~n
d }~0 0 |D ]Î}
|
j
d kr¾z²t|
jˆƒrà|}n8t|
jˆƒrð|}t|
jˆƒr|}t|
jˆƒr|
jj
}| d¡}t|ƒt|ƒkr||t|
j
ƒt|
jƒt|
jd |
j ƒt|
jƒt|ƒg}| |¡ |d7 }W q¾   Y q¾0 q¾qH|rÜtdd
ddd$}ˆ |¡}| |¡ W d   ƒ n1 sÒ0    Y  td|ƒ |  ¡  tƒ  d S )Nr­   r®   r¯   r·   r±   r.   r   rµ   Tr¶   r‰   r°   rO   r  rV   r  zcounting : r  r  r  r   r   r     sR    



"

$ÿ


*
zweeklyfilter.<locals>.nfilterz
Enter the week for filter :é   r®   r·   r¦   r˜   r§   rS   r1   r2   r¨   r©   r«   r0   z
Login Doner¸   zPlease Enter A Vailed Groupc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S r¹   r»   r½   r¿   r   r   rÀ   í  s    

,zweeklyfilter.<locals>.mainc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S rÁ   r»   r½   r¿   r   r   rÃ     s    

,zweeklyfilter.<locals>.main1rÂ   r    rP   rQ   r°   rO   rM   rT   r±   r.   rÄ   rÅ   rÆ   rÇ   rº   r
  rÈ   r  r  r   r  r   ÚweeklyfilterŽ  sr    $,



*
n

r  c            >         s  ddl m} m} dd l}dd l }ddl m}m} m} ddlm} ddlm	}m
}m}	m}
m
}m}m}
 dd l}ddlm}m}m}m} ddlm}m} dd l‰ dd l}dd l}dd l}dd l}ddlm}m}m} |j d	d
 t!ƒ  dd l"}dd l}dd l#}|j$|j%d | &¡ }| 'd¡ |d
 d  (¡ }d} d}!|d
 d  (¡ }"t)dddd(}#ˆ  *|#¡}$dd„ |$D ƒ}%W d   ƒ n1 s€0    Y  t)dddd(}#ˆ  *|#¡}$dd„ |$D ƒ}&W d   ƒ n1 sÈ0    Y  | d|"› | |!ƒ}'|' +¡  |' ,¡ s
t-d|"› dƒ n¸g }(d })d}*g }+d},|,dkrÂz |' .|¡}-|-j/d	kr0t0|-j1ƒ}.|'j2|-d	d}/g }0g }1d}2g }3|/D ]F}4z*t0|4j1ƒ|&v rš|3 3|& 4t0|4j1ƒ¡¡ W n   t-dƒ Y n0 qn|# 5¡  |' 6¡  |3j7d	d  |3D ]}5|%|5= qÖt)dd!dd"d#$}#ˆ  8|#¡}6|6 9|%¡ W d   ƒ n1 s 0    Y  d},nt-|j:|j; d$ ƒ d},W nr |j<j=j>yp   |'||ƒƒ Y nN t?yš   t-|j:|j@ d% ƒ d},Y n$   t-|j:|j; d& ƒ d},Y n0 qtAƒ }7‡ fd'd(„}8‡ fd)d*„}9|8ƒ  |9ƒ  t)d+dd,dª}:ˆ  *|:¡};t)dd!d,dp}#ˆ j8|#d-d.d/}<|< Bg d0¢¡ d}5|;D ]8}=|5d17 }5|< B|5|=d1 |=d2 |=d3 |=d4 |=d5 f¡ q<W d   ƒ n1 sŒ0    Y  W d   ƒ n1 s¬0    Y  | Cd6¡ | Cd+¡ t-|j:|jD d7 ƒ t-|j:|j@ d8 ƒ t-|j:|jE d9 ƒ tFƒ  d S ):Nr   rû   )rþ   r"   Úevents©ÚGetDialogsRequestr›   ©ÚGetChannelsRequestÚGetFullChannelRequestrš   ÚInviteToChannelRequestr£   r   Tr   r©   r¦   r˜   ÚToGroupr1   r2   r¨   r°   r    r  rQ   c                 S   s   g | ]}|‘qS r   r   ©r*   rn   r   r   r   r,   N  r-   z!Deletealready.<locals>.<listcomp>c                 S   s   g | ]}t |d  ƒ‘qS )rÄ   )r[   r  r   r   r   r,   R  r-   r0   z
Login fail, for number z need Login first
éÈ   éÿÿÿÿr¶   zError get user)ÚreverserO   rV   r  z
Invalid Group..
z
Only Public Group Allowed..
z
Invalid Group....
c                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S r¹   r»   r½   r¿   r   r   rÀ   †  s    

,zDeletealready.<locals>.mainc                     sº   t ƒ } tddddJ}ˆ  |¡}|D ]*}|  |¡ |D ]}|dkr6|  |¡ q6q$W d   ƒ n1 sd0    Y  tdddd*}ˆ j|dd	d
}| | ¡ W d   ƒ n1 s¬0    Y  d S rÁ   r»   r½   r¿   r   r   rÃ   š  s    

,zDeletealready.<locals>.main1rÂ   rP   rS   rM   rT   r±   r.   rÄ   rÅ   rÆ   rÇ   rº   zAlready Member Deleted Done !zTask CompletedúPress Enter to exit)Gr5   r"   rü   rÉ   rþ   r  rö   r  rË   rœ   r   rž   rŸ   r    r¡   r¢   r  rÊ   r  r  rš   r  r¤   r¥   r6   r   r   r7   r8   r   r   r   r   r9   r“   rY   rÐ   rÑ   rÌ   rÍ   rÎ   r:   r&   r}   r~   r   rÔ   Z	megagroupr[   r‹   rÖ   rZ   ÚindexrÜ   r?   Úsortr_   r`   r<   rŽ   ÚerrorsZrpcerrorlistÚChatWriteForbiddenErrorÚ
ValueErrorr=   r¼   rÓ   ra   r@   rA   rB   )>r"   rü   rÉ   r5   rþ   r  r  rœ   r   rž   rŸ   r    r¡   r¢   r  r  r  rš   r  r¤   r¥   r   r   r7   r8   r   r   r   r“   rY   rÝ   rå   rß   rà   rG   rC   Zusers1ÚusersZuserlistrH   ZchatsZ	last_dateZ
chunk_sizeÚgroupsr   r´   Zgroup_idrç   ÚresultsZresults1rá   Zindex1rè   rn   r   r¾   rÀ   rÃ   rë   rì   r_   r+   r   r¿   r   Ú
Deletealready*  s¸    $

.
.





*
n

r)  c                     sà  ddl m‰ dd l‰ddlm}  ddlm}m}m}m	} ddl
m}m}m
}m} ddlm}	 ddlm}
m‰m‰m‰ dd l}ddl
m}m}
m} dd l}dd l‰	dd l‰
dd	lm‰ dd
lm} ddl m!}m"‰  |ƒ  ˆ j#‰ˆ j$}ˆ j%‰ˆ j&‰ˆ j'‰‡	fdd
„}|ƒ  t(ƒ  g }g }g }t)ddƒ>}ˆ|ƒ}t*|ƒ}|D ]}| +t,|d ƒ¡ q8W d   ƒ n1 sh0    Y  |‰
t-|› dˆ› dˆ› t.t/|ƒƒ› ˆ› ƒ ‡ ‡‡‡‡‡‡‡‡	‡
‡‡‡
‡‡fdd„‰‡‡‡fdd„‰ˆƒ  d S )Nr   r!   r  ©rœ   ÚInputPeerChannelÚ
InputPeerUserr¡   ©ÚPeerFloodErrorÚUserPrivacyRestrictedErrorr$  ÚUserAlreadyParticipantError©r  ©r‡   r$   r#  r†   ©ÚUsernameInvalidErrorÚChannelInvalidErrorrK   r%   ©Ú
StringSessionr   c                      s$   ˆ j dkrˆ  d¡ n
ˆ  d¡ d S ©NÚntÚclsÚclear©r³   Úsystemr   ©rY   r   r   Úclrâ  s    
zaddcontactforphone.<locals>.clrr'   r    úTotal account: r‰   c                      s>  t tˆ› dˆ› ƒƒd } t tˆ› dˆ› ƒƒ}t tˆ› dˆ› ƒƒ}t tˆ› dˆ› ƒƒ}tdddd	2}ˆj|d
dd}| ||| g¡ W d   ƒ n1 s¢0    Y  d
}d
}ˆ	| |… D ]f}|d7 }td|› ƒ ˆ
 |¡}	ttjˆ j	 dtj
› dtjˆ j › d|	›  ƒ ˆd|	› ddƒ}
|
 ¡  |
 
¡ sftˆ
› dˆ› ƒ |
 |	¡ |
 |	tdƒ¡ d}g }t|dd	x}
ˆj|
d
dd}t|d ƒ |D ]H}i }|d
 |d< |d |d< t |d ƒ|d< |d |d< | |¡ qšW d   ƒ n1 sú0    Y  tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 sR0    Y  t |ƒ}|| }tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 sº0    Y  t |ƒ}|| }tdddd	.}ˆj|d
dd}| ||g¡ W d   ƒ n1 s0    Y  d
}|D ]ô}t |ƒt |d ƒkr*t |d ƒt |ƒkr*z^|d7 }|d dkrŠtˆ
› dˆ› ƒ W q*|
ˆjj|d |d dd d!d"ƒ |› d#}W nZ ˆjyè } z|jj}W Y d }~n4d }~0    ˆ ¡  tˆ› d$ˆ› ƒ Y q*Y n0 t|ƒ q*|d7 }qÀˆ d¡ ˆƒ  d S )%NúFrom Account No : r.   úUpto Account No : zFrom where you want to start : z3How many contacts you want to add in one Account : ú
memory.csvrO   rP   rQ   rS   rM   rT   r   úIndex : r/   r‰   r0   r1   r2   úsome thing has changedúEnter the code: r°   Úsrnor²   rÄ   r‹   rÅ   r³   r    rV   úno username, moving to nextZgdfT)r‹   r×   r  rG   Zadd_phone_privacy_exceptionú - doneúUnexpected Error)r|   rB   r:   r_   rÓ   r   r;   r   r<   r=   r”   r@   r}   r~   rø   rù   r&   ÚnextrZ   r¼   r•   ZAddContactRequestÚRPCErrorÚ	__class__Ú__name__Ú	print_excra   ) ÚFromÚUptoÚrexÚhacksÚfiler_   r	  ÚindexxÚxdrG   rH   Ú
input_filer&  rC   Úrowsr+   rè   Úhash_objÚ
csv_readerÚlist_of_rowsÚ
row_numberÚ
col_numberÚnumnextÚ	startfromÚ	nextstartÚnumendÚendtoÚnextendÚdfÚitrÙ   ræ   )r   r"   ÚagainÚblr6   r#  r†   r   rY   rF   r    r&   Ú	tracebackr$   Úyer   r   Úautosü  sš    0
0


.44.,û

z!addcontactforphone.<locals>.autosc                     s,   t ˆ› dˆ› ƒ} | dkr"ˆ ƒ  ntƒ  d S )NzRDone!
Choose From Below:

1 - Repeat The Script
OR Just Hit Enter To Quit

Enter: Ú1)rB   Úquit)Ústat)rj  r   r    r   r   rf  e  s    z!addcontactforphone.<locals>.again)0r4   r"   r6   rö   r  rË   rœ   r+  r,  r¡   r{   r.  r/  r$  r0  rÊ   r  r5   r‡   r$   r#  r†   r7   r4  r5  rK   ÚrerY   rh  r&   Útelethon.sessionsr7  r8   r   r   ÚLIGHTRED_EXr=   r@   ÚBLUErA   r9   r:   ÚtuplerZ   r|   r   r[   Úlen)r  rœ   r+  r,  r¡   r.  r/  r$  r0  r  r‡   r7   r4  r5  rK   rn  r7  r   Úgrr?  r   r€   rG   Ú	delta_objrZ  Ú
list_of_phoneÚphone_r   )r   r"   rf  rj  rg  r6   r#  r†   r   rY   rF   r    r&   rh  r$   ri  r   ÚaddcontactforphoneÅ  sJ    6((irx  c                  C   s`   dd l } ddl m}m}m} | jdd tƒ  t|j|j d ƒ t|j|j d ƒ t	ƒ  d S )Nr   r   Tr   z-Go to Addcon folder and Run Automarge.py filer   )
r8   r   r   r   r   r9   r   r<   rA   rB   )r8   r   r   r   r   r   r   Úforpcn  s    ry  c            "      C   sP  ddl m}  dd l}tƒ  ddlm}m}m} ddlm	} ddl
m}m}m
} dd l}	ddlm}
m}m}m}
 ddlm} ddlm}m} dd	lm} dd l}dd
lm}m}m} |jdd td
dƒ$}dd„ |  |¡D ƒa!W d   ƒ n1 sò0    Y  t"dt#t$t!ƒƒ ƒ t%t&dƒƒd }t%t&dƒƒ}d}da't!||… D ]}|d7 }t"d|› ƒ | (|¡}t"d|› ƒ | d|› ddƒ}| )|¡ ||ddƒ}d}|j*D ]ž}|d7 }z6|||gdƒ t"|j+|j, |› d|j-› d ƒ W nX |j.yB }  z<| j/j0}!t"|› d|j-› d|!› ƒ W Y d } ~ q¨W Y d } ~ n
d } ~ 0 0 q¨q@d S )Nr   r!   r3  rî   ©r‡   r$   r#  r  ©r¢   )ÚGetContactsRequestÚDeleteContactsRequest©ÚAddChatUserRequestr   Tr   r'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,     r-   z!Deletecontact.<locals>.<listcomp>r@  rA  r.   rB  rD  r/   r0   iDD  Z5bdea166e6097ce98a23©ÚhashrŠ   ú - z	 - DELETE)1r4   r"   r6   r9   r{   r4  r5  rK   rö   rï   r5   r‡   r$   r#  rn  rÊ   r  r  rš   r  rË   r¢   Útelethon.tl.functions.contactsr|  r}  r  r8   r   r   r   r   r:   r&   Úphlistr   r[   rs  r|   rB   Zrexhackspror;   r>   r&  r<   r=   r‹   rL  rM  rN  )"r"   r6   r4  r5  rK   rï   r‡   r$   r#  rn  r  r  rš   r  r¢   r|  r}  r  r8   r   r   r   rC   ÚRexhacks_ne_script_banaya_haiÚ2telegram_script_banyane_ke_liye_rexhacks_ko_dm_krorU  ZrexhacksonytrG   rH   r•   ZrexaddZrexopræ   Úerror   r   r   Ú
Deletecontactx  sN    2


&rˆ  c                  C   sX   dd l } g d¢}|D ]}t|  t¡› |› t› ƒ qtdƒ tdƒ tdƒ tdƒ d S )Nr   r	   r   z6========================= Buy Tools  : T.me/Tohaputra
r   r   )r
   r   r   r
   r   r   r   r   r   r   r9   ª  s    r9   c            8      C   sš  dd l } ddl m}m}m} | jdd tƒ  ddlm} dd l}ddl	m
}m}m} ddl
m}	 ddlm}
m}m} dd l}
dd l}dd	lm} dd
lm}m}m}m} ddlm} ddlm} dd
l
m} ddl m}m}m} dd l }| !¡ }| "d¡ |d d }|d d }|d d }|d d }|d d }t#ddƒ$}dd„ | $|¡D ƒ}W d   ƒ n1 sn0    Y  t%dt&t'|ƒƒ ƒ t%|j(|j) d ƒ t*ƒ } t%|j(|j) d ƒ t+t*ƒ ƒ}!t%|j(|j) d ƒ t+t*ƒ ƒ}"| dkrút+|ƒ}#|}$n| dkrt+|ƒ}#|}$t+|ƒ}%t+|ƒd }&t+|ƒ}'d}(da,||&|'… D ]R})|(d7 }(| -|)¡}*t%d |*› ƒ |d!|*› d"d#ƒ}+|+ .|*¡ t%d$|(› ƒ z|+ /||#ƒ¡},W nh t0y
   | dkrØ|+|	|$ƒƒ |+ 1||#ƒ¡},n.| dkr|+||$ƒƒ | 2d%¡ |+ 1||#ƒ¡},Y n0 |+||,d&ƒ}-t+|-j3j4ƒa,t%d't,› ƒ t,|%krZt%d(|%› d)ƒ t*ƒ  t5ƒ  |+|dd*ƒ}.|.j6}/t'|/ƒ}0t%d+|0› ƒ d}1d}2|1|0k r@d,d„ |/d |!… D ƒ}3z–| 2|"¡ |+|j7j|#|3d-ƒ |1|!7 }1t8dd.ƒD ]F}4z
|/|4= W n4 t9y  }5 zW Y d }5~5qÞW Y d }5~5n
d }5~50 0 qÞt%|j(|j) d/|1›  ƒ W nJ |j:yŒ }6 z.|6j;j<}7t%t&|7ƒƒ W Y d }6~6q@W Y d }6~6n
d }6~60 0 qŒq@d S )0Nr   r   Tr   r!   r3  rî   rz  ©r†   r  r{  ©r|  r~  r¦   r˜   r  ÚGroupIDÚ	EnterStopÚStartingAccountÚ
EndAccountr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   å  r-   zbulkadder.<locals>.<listcomp>r@  ú1Enter Y if group has private link else N (Y/N) : z.In A Batch How many Members You Want To Add : ú*Enter Delay Time Per Request 0 For None : ÚYÚNr.   r/   r0   iùÜ" Z 85468d44607fcb5b9efe5ed61e4582a2rD  rÇ   ©Úchannelú	Members: úThe Goal Of ú Has Been Completedr€  zTotal : c                 S   s   g | ]}|‘qS r   r   )r*   Zdeltar   r   r   r,     r-   ©r”  r&  é
   zBATCH: )=r8   r   r   r   r   r9   r4   r"   r6   r{   r4  r5  rK   rö   rï   r5   r‡   r$   r#  rn  r   r†   rÊ   r  r  rš   r  rË   r¢   rƒ  r|  r  r7   rÌ   rÍ   r:   r&   r   r[   rs  r<   r=   rB   r|   ZLegenddev_is_main_developerr;   r>   rÔ   r%  Úget_input_entityr   Ú	full_chatÚparticipants_countrl  r&  ÚchannelsÚrangerÕ   rL  rM  rN  )8r8   r   r   r   r"   r6   r4  r5  rK   rï   r‡   r$   r#  rn  r   r†   r  r  rš   r  r¢   r|  r  r7   rÝ   Ú	grouplinkÚgroupidÚstopnumÚstacnoÚendacnorC   r„  ÚprchkZLegenddevismainr˜   r‹   ÚprlinkÚstopZ
start_fromZuptorU  ZpythondeveloperrG   rH   r”  ÚchannelinfoÚmembersZuser_to_addZcountconZ
batchcountZlolZsemenrn   ÚDræ   r‡  r   r   r   Ú	bulkadderÂ  s¼    
4











þ
(rª  c            1      C   s  dd l } ddl m}m}m} | jdd tƒ  ddlm} dd l}ddl	m
}m}m} ddl
m}	 ddlm}
m}m} dd l}
dd	lm}m}m}m} dd
lm} ddlm} ddl
m} ddl m}m}m} dd l}dd l}|  ¡ }| !d
¡ |d d }|d d }|d d }|d d }|d d }t"ddƒ$}dd„ | #|¡D ƒ}W d   ƒ n1 sb0    Y  t$dt%t&|ƒƒ ƒ t$|j'|j( d ƒ t)ƒ }t$|j'|j( d ƒ t*t)ƒ ƒ} |dkrÐt*|ƒ}!|}"n|dkræt*|ƒ}!|}"t*|ƒ}#t*|ƒd }$t*|ƒ}%d}&da+||$|%… D ]ê}'|&d7 }&t$d|&› ƒ | ,|'¡}(t$d|(› ƒ |d |(› d!d"ƒ})|) -|(¡ z|) .||!ƒ¡}*W nh t/yà   |dkr®|)|	|"ƒƒ |) 0||!ƒ¡}*n.|dkrÜ|)||"ƒƒ | 1d#¡ |) 0||!ƒ¡}*Y n0 |)||*d$ƒ}+t*|+j2j3ƒa+t$d%t+› ƒ t+|#kr0t$d&|#› d'ƒ t)ƒ  t4ƒ  |)|dd(ƒ},d}-|,j5D ]¶}.|-d7 }-zB|)||!|.gd)ƒ t$|j'|j( |-› d*|.j6› d+ ƒ | 1| ¡ W nd |j7yú }/ zH|/j8j9}0t$|j'|j: |-› d*|.j6› d*|0›  ƒ W Y d }/~/qHW Y d }/~/n
d }/~/0 0 qHqd S ),Nr   r   Tr   r!   r3  rî   rz  r  r{  rŠ  r~  r¦   r˜   r  r‹  rŒ  r  rŽ  r'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   P  r-   zsingle.<locals>.<listcomp>r@  r  r  r‘  r’  r.   rD  r/   r0   éî + Ú 5f34bd560b5053ae7edc32b5c0246245rÇ   r“  r•  r–  r—  r€  r˜  r‚  z - DONE);r8   r   r   r   r   r9   r4   r"   r6   r{   r4  r5  rK   rö   rï   r5   r‡   r$   r#  rn  rÊ   r  r  rš   r  rË   r¢   rƒ  r|  r  r   r7   rÌ   rÍ   r:   r&   r   r[   rs  r<   r=   rB   r|   ZRExhackspror;   r>   rÔ   r%  rš  r   r›  rœ  rl  r&  r‹   rL  rM  rN  rŽ   )1r8   r   r   r   r"   r6   r4  r5  rK   rï   r‡   r$   r#  rn  r  r  rš   r  r¢   r|  r  r   r7   rÝ   rŸ  r   r¡  r¢  r£  rC   r„  r¤  r˜   r‹   r¥  r¦  r…  r†  rU  ZdeltaxdrG   rH   r”  r§  r•   ZdeltaaddZdeltaopræ   r‡  r   r   r   Úsingle1  sœ    
4









"&r­  c                  C   s†  dd l } ddl m}m}m} | jdd tƒ  ddlm} ddlm	}m
} ddlm} ddlm} dd l}ddlm
}	 dd l}
ddl m}m}m} dd l}dd l}dd l}
dd l}d	}td
dƒž}dd
„ | 
|¡D ƒ}d}|D ]p}| |¡}|d7 }t|j|j d|›  ƒ |d|› ddƒ}| |¡ ||jj| d¡dƒ}tdƒ d}qÞW d   ƒ n1 sf0    Y  t|r|dndƒ d S )Nr   r   Tr   r!   r…   r#   r%   Fr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   œ  r-   zsetprofile.<locals>.<listcomp>r.   úChanging in r0   r«  r¬  zset.jpg)rT  z"done! profile pic has been changedrz   r3   )r8   r   r   r   r   r9   r4   r"   r5   r†   r‡   r$   r6   r&   r7   r’   r“   r   rY   r:   r;   r   r<   r=   r>   ZphotosZUploadProfilePhotoRequestZupload_filerB   )r8   r   r   r   r"   r†   r‡   r$   r6   r&   r7   r’   r“   r   rY   rI   rC   rD   rE   rF   rG   rH   Úresultr   r   r   Ú
setprofileŠ  s:     

ÿ&r°  c                  C   s˜  dd l } ddl m}m}m} | jdd tƒ  ddlm} ddlm	}m
} ddlm} ddlm} ddlm
} dd l}	dd	lm}
 dd l}ddl m}m}m} dd l}dd l}
dd l}dd l}d
}tddƒ¤}d
d„ |	 |¡D ƒ}d}|D ]v}| |¡}|d7 }t|j|j d|›  ƒ |d|› ddƒ}| |¡ ||| d¡ƒƒ t|j|j d ƒ d}qêW d   ƒ n1 sx0    Y  t|rŽdndƒ d S )Nr   r   Tr   r!   r…   )ÚDeletePhotosRequestr#   r%   Fr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   ¾  r-   z!Deleteprofile.<locals>.<listcomp>r.   zDeleting in r0   r«  r¬  ÚmezProfile Pic Deletedrz   r3   )r8   r   r   r   r   r9   r4   r"   r5   r†   r‡   Ztelethon.tl.functions.photosr±  r$   r6   r&   r7   r’   r“   r   rY   r:   r;   r   r<   rŽ   r>   Zget_profile_photosr=   rB   )r8   r   r   r   r"   r†   r‡   r±  r$   r6   r&   r7   r’   r“   r   rY   rI   rC   rD   rE   rF   rG   rH   r   r   r   Ú
Deleteprofile«  s8     

&r³  c                     s  dd l } ddl m‰m}m‰ | jdd tƒ  ddlm‰ ddlm	} ddl
m}m}m
}m} ddlm‰m‰
m‰ m‰	 dd	lm‰ dd
lm‰m‰ ddlm‰ ddlm}m‰m‰ dd l}dd l}	dd l ‰
dd
l m!}
 dd l"‰dd l#‰dd l$‰dd l } ddl m‰m}m‰ | jdd ddl%m&} t'ˆj(ˆj) d ƒ t*t+ƒ ƒ}t,ddƒ<}
|
|
ƒ}t-|ƒ}|}d}||d  |d  }W d   ƒ n1 sŽ0    Y  t*dƒ‰t.dƒ‰|‰| /¡ }| 0d¡ |d d ‰‡ ‡‡‡‡‡‡‡‡‡	‡
‡‡‡
‡‡‡‡‡‡‡fdd„}|ƒ  d S )Nr   r   Tr   r!   r  r*  r-  r1  ©r  rš   rð   rz  r%   r6  ú'Which Account You Want To Use?

Enter: r'   r    r.   r«  r¬  r¦   r˜   r  c                     s  ˆ} ˆ  ˆ¡}ˆd|› ˆˆƒ}| ¡  | ¡ sz0| |¡ | |tdƒ¡ tdƒ | |¡ W n. ˆyŽ   tdƒ}tdƒ |j|d Y n0 | ¡ }|js¦|j	}n|j	d |j }d}g }t
|dd	v}ˆ
j|d
dd}	t|	d ƒ |	D ]F}
i }|
d
 |d< |
d |d< t
|
d ƒ|d< |
d |d< | |¡ qêW d   ƒ n1 sH0    Y  t
tdƒƒ}t
tdƒƒ}|D ]¢}t
|ƒt
|d ƒkræt
|d ƒt
|ƒkræzpd}
|d dkrÂtdƒ W qn|ˆ| |d gƒƒ ˆjˆj d }
tˆjˆj d ƒ ˆ ˆ dd¡¡ W n\ ˆ
yH   ˆjˆj d }
ˆ ˆ dd¡¡ Y n& ˆ	y`   d}
Y n ˆy® } z6d }
tˆjˆj d! ƒ ˆ ˆ d"d#¡¡ W Y d }~nÈd }~0  ˆ yö } z0|ˆ| ƒƒ ˆ d¡ W Y d }~qnW Y d }~n€d }~0  ˆjy$ } z|jj}
W Y d }~nRd }~0  tyL } z|}
W Y d }~n*d }~0    ˆ ¡  td$ƒ Y qnY n0 | | ¡}|ˆ|d%ƒ}t
|jjƒ}tˆjˆj d|› dˆjˆj › d&|› ˆj› dˆjˆj › d'|d › d(|
› 
 ƒ n*t
|d ƒt
|ƒkrntd)ƒ tƒ  t ƒ  qnd S )*Nr0   rò   rV   ró   rô   r‰   r°   rP   rQ   rS   rM   rT   r   rG  r.   r²   rÄ   r‹   rÅ   r³   ú
Start From = ú	End To = r˜   rH  ÚDONEzPlease Wait...é   é   ÚPrivacyRestrictedErrorrÇ   ÚALREADYr.  z(Script Are In Progress So Please Wait...é<   éZ   rJ  r“  z > Group Members ú>> ú >> zMembers Added Successfully!)!r;   r}   r~   rø   rù   rB   r   Úget_mer  r×   r:   r&   rK  r|   rZ   r<   r=   rA   r   Ú	randrangerŽ   rL  rM  rN  rÕ   rO  rÔ   r›  rœ  r@   r”   ÚCYANÚexit)Úchannel_usernamerG   rH   rõ   rè   Ú
LegendNamerW  r&  rC   rX  r+   r_  rb  rÙ   ÚgÚcwferæ   ÚdZchannel_connectZchannel_full_infoZcountt©r$  r   r  r  rš   r.  rñ   r   r"   r0  r/  r€   r   r6   r#  rF   r
   r   Úto_grouprh  r$   r   r   rj  ù  s    


,
,
&
"
TzAdder.<locals>.autos)1r8   r   r   r   r   r9   r4   r"   rö   r  rË   rœ   r+  r,  r¡   r{   r.  r/  r$  r0  rÊ   r  r  rš   r÷   rñ   r5   r‡   r$   r#  r7   r   r6   r&   rh  r   r
   ro  r7  r   r<   rA   r|   rB   r:   r¼   r[   rÌ   rÍ   )r8   r   r  rœ   r+  r,  r¡   r‡   r7   r   r&   r7  ÚLegend_devinputÚread_objrZ  r[  r\  r]  ÚvaluerÝ   rj  r   rÊ  r   ÚAdderÊ  sN    
4
4^rÏ  c            !         sô  ddl m‰ ddlm} m‰m‰m} dd l‰ddlm	‰ ddl
m}m‰ ddlm
}m}m}m} ddlm}m}m‰ m}	 ddlm} dd	lm}
m‰m‰
m‰ dd l}dd
lm}m}
m} dd l}dd l ‰dd l!‰ddlm"‰ ddl#m$} dd
l%m&}m'‰ dd l(‰dd l)}|ƒ  ˆj*‰ˆj+}ˆj,‰ˆj-}ˆj.‰‡fdd„}|ƒ  dd l%}ddl%m'‰m/}m0‰ |j&dd t1ƒ  | 2¡ }| 3d¡ |d d ‰
|d d ‰|d d ‰|d d ‰|d d ‰	g }t4ddƒ>}ˆ|ƒ}t5|ƒ}|D ]}| 6t7|d ƒ¡ qÞW d   ƒ n1 s0    Y  |‰t8|› dˆ› dˆ› t9t:|ƒƒ› ˆ› ƒ ‡ ‡‡‡‡‡‡‡‡	‡
‡‡‡
‡‡‡‡‡‡‡‡‡‡‡fdd„}‡ ‡‡‡‡‡‡‡‡	‡
‡‡‡
‡‡‡‡‡‡‡‡‡‡‡fd d!„}t9t;|› d"ˆ› ƒƒ} | d#krà|ƒ  n| d$krð|ƒ  d S )%Nr   r!   r  r{  )r  rï   r*  r-  r1  r2  r3  r%   r6  r   c                      s$   ˆ j dkrˆ  d¡ n
ˆ  d¡ d S r8  r<  r   r>  r   r   r?  v  s    
zadderforphone.<locals>.clrr   Tr   r¦   r˜   r  r‹  rŒ  r  rŽ  r'   r    r@  r‰   c            )         sæ  t ˆjˆj d ƒ ttƒ ƒ} d}tˆƒ}tˆƒ}tˆƒd }tˆƒ}tdƒ}tdƒd }tˆƒ}tdddd2}	ˆj|	d	d
d}
|
 ||| g¡ W d   ƒ n1 s¨0    Y  d}d}ˆ||… D ]}
|d7 }t d
|› ƒ ˆ 	|
¡}t d|› ƒ ˆd|› ddƒ}| 
¡  | ¡ sJt ˆ› dˆ
› ƒ | |¡ | 
|tdƒ¡ |}g }t|ddx}ˆj|d	d
d}t|d ƒ |D ]H}i }|d |d< |d |d< t|d ƒ|d< |d |d< | |¡ q~W d   ƒ n1 sÞ0    Y  tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 s60    Y  t|ƒ}|| }tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 sž0    Y  t|ƒ}|| } tdddd.}!ˆj|!d	d
d}
|
 || g¡ W d   ƒ n1 sü0    Y  |ˆ|ƒƒ ˆ d¡ | ˆ|ƒ¡}"|ˆ|"dƒ}#t|#jjƒ}$t d|$› ƒ |$|krxt d|› dƒ tƒ  tƒ  d}%|D ]J}t|ƒt|d ƒkr€t|d ƒt|ƒkr€zb|%d7 }%|d d krât ˆ› d!ˆ
› ƒ W q€|ˆ
j ||d g¡ƒ t |%› d"ƒ ˆ | ¡ W n´ ˆ y^ }& z0|ˆ|ƒƒ ˆ d¡ W Y d }&~&q€W Y d }&~&ntd }&~&0  ˆ	jyž }' z&|'jj}(t |%› d#|(› ƒ W Y d }'~'n4d }'~'0    ˆ ¡  t ˆ› d$ˆ
› ƒ Y q€Y n0 q€|d7 }qÆˆ d¡ d S ©%Nr  r°   r.   é2   rC  rO   rP   rQ   rS   rM   rT   r   rD  r/   r0   r1   r2   rE  rF  rG  r²   rÄ   r‹   rÅ   r³   r    rÇ   r“  r•  r–  r—  rV   rH  rI  r‚  rJ  ©r   r<   r=   r|   rB   r[   r:   r_   rÓ   r;   r}   r~   rø   rù   r&   rK  rZ   r¼   r   rš  r›  rœ  rl  r  r  rL  rM  rN  rO  ra   ©)r˜   r‚   Zrexlinkr‹   rP  rQ  rR  rS  r¦  rT  r_   r	  rU  rV  rG   rH   rW  r&  rC   rX  r+   rè   rY  rZ  r[  r\  r]  r^  r_  r`  ra  rb  rc  rd  r”  r§  Zrexprodeltanoobre  rÈ  ræ   rÙ   )r$  r   r  rš   r¢   r   r"   r6   r£  r#  r†   r   rŸ  r   rY   rF   r    r&   r¢  r¡  r   rh  r$   ri  r   r   rj  ˜  s¶    
0



.44.


,
"&
zadderforphone.<locals>.autosc            )         sô  t ˆjˆj d ƒ ttƒ ƒ} d}tˆƒ}tˆƒ}tˆƒd }tˆƒ}tdƒ}tdƒd }tˆƒ}tdddd2}	ˆj|	d	d
d}
|
 ||| g¡ W d   ƒ n1 s¨0    Y  d}d}ˆ||… D ]}
|d7 }t d
|› ƒ ˆ 	|
¡}t d|› ƒ ˆd|› ddƒ}| 
¡  | ¡ sJt ˆ› dˆ
› ƒ | |¡ | 
|tdƒ¡ |}g }t|ddx}ˆj|d	d
d}t|d ƒ |D ]H}i }|d |d< |d |d< t|d ƒ|d< |d |d< | |¡ q~W d   ƒ n1 sÞ0    Y  tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 s60    Y  t|ƒ}|| }tddƒ<}ˆ|ƒ}t|ƒ}d}d}||d  |d  }W d   ƒ n1 sž0    Y  t|ƒ}|| } tdddd.}!ˆj|!d	d
d}
|
 || g¡ W d   ƒ n1 sü0    Y  |ˆ|ƒƒ ˆ d¡ | ˆ|ƒ¡}"|ˆ|"dƒ}#t|#jjƒ}$t d|$› ƒ |$|krxt d|› dƒ tƒ  tƒ  d}%|D ]X}t|ƒt|d ƒkr€t|d ƒt|ƒkr€t d|$› ƒ zb|%d7 }%|d d krðt ˆ› d!ˆ
› ƒ W q€|ˆ
j ||d g¡ƒ t |%› d"ƒ ˆ | ¡ W n´ ˆ yl }& z0|ˆ|ƒƒ ˆ d¡ W Y d }&~&q€W Y d }&~&ntd }&~&0  ˆ	jy¬ }' z&|'jj}(t |%› d#|(› ƒ W Y d }'~'n4d }'~'0    ˆ ¡  t ˆ› d$ˆ
› ƒ Y q€Y n0 q€|d7 }qÆˆ d¡ d S rÐ  rÒ  rÓ  )r$  r   r  rï   r¢   r   r"   r6   r£  r#  r†   r   rŸ  r   rY   rF   r    r&   r¢  r¡  r   rh  r$   ri  r   r   Úprivate  s¸    
0



.44.


,
"&
zadderforphone.<locals>.privatez%Press Y if group is private else N : r‘  r’  )<r4   r"   rÊ   r  r  rš   r  r6   rË   r¢   rö   r  rï   rœ   r+  r,  r¡   r{   r.  r/  r$  r0  r5   r‡   r$   r#  r†   r7   r4  r5  rK   rn  rY   rh  r&   ro  r7  r8   r   r   r   r
   rp  r=   r@   rq  rA   r   r   r9   rÌ   rÍ   r:   rr  rZ   r|   r   r[   rs  rB   )!r  r  r  rœ   r+  r,  r¡   r.  r/  r0  r‡   r7   r4  r5  rK   rn  r7  r   r
   rt  rg  r?  r8   r   rÝ   rG   ru  rZ  rv  rw  rj  rÔ  Z	rexchooser   )r$  r   r  rï   rš   r¢   r   r"   r6   r£  r#  r†   r   rŸ  r   rY   rF   r    r&   r¢  r¡  r   rh  r$   ri  r   Ú
adderforphoneX  sj    
6(:y:y

rÕ  c                  C   sÞ   dd l } dd l}ddlm}m}m} dd l}dd l}tƒ  tdddd.}|j	|ddd	}| 
g d
¢¡ W d   ƒ n1 s|0    Y  ttdƒƒd }	d}
|
|	krÆ| j
d
| jd |
d }
| d¡ qš| d¡ t d¡ d S )Nr   r   rC  rO   rP   rQ   rS   rM   rT   ©r.   r.   rÑ  ú*How many accounts do you want to run ? => r.   zpython v1-1.py©Z
creationflagsrÅ   r™  )r’   r8   r   r   r   r   r6   r9   r:   r_   rÓ   r|   rB   ÚPopenÚCREATE_NEW_CONSOLEr   rY   ra   ©r’   r8   r   r   r   r   r6   rT  r_   r	  rj   r   r   r   Ú
multipleadder  s"    ,
rÜ  c                     s.  dd l } ddl m‰m}m‰ | jdd tƒ  ddlm‰ ddlm	‰  ddl
m} ddlm
}m}m}m} dd	lm‰m‰m}m‰ dd
lm} ddlm}	m}
 ddlm‰ dd
lm}m‰m‰ dd l}dd l }
ddl!m"} dd l#‰
ddl#m$} dd l%‰dd l&‰dd l'‰dd l } ddl m‰m}m‰ | jdd ddl(m)} t*ˆj+ˆj, d ƒ t-t.ƒ ƒ}t/ddƒ<}||ƒ}t0|ƒ}|}d}||d  |d  }W d   ƒ n1 s¦0    Y  t-dƒ‰	t1dƒ‰|‰| 2¡ }| 3d¡ |d d ‰|‰
|d d ‰‡ ‡‡‡‡‡‡‡‡‡	‡
‡‡‡
‡‡‡‡‡‡fdd„}|ƒ  d S )Nr   r   Tr   r!   )ÚFloodWaitErrorr  r*  r-  r1  r´  rð   rz  )ÚMessager%   r6  rµ  r'   r    r.   r«  r¬  r¦   r˜   r  ZMessage_filec                     sÎ  ˆ} ˆ
}ˆ  ˆ¡}ˆd|› ˆ	ˆƒ}| ¡  | ¡ s”z0| |¡ | |tdƒ¡ tdƒ | |¡ W n. ˆy’   tdƒ}tdƒ |j|d Y n0 | ¡ }|jsª|j	}n|j	d |j }d}g }t
|dd	v}	ˆ
j|	d
dd}
t|
d ƒ |
D ]F}i }|d
 |d< |d |d< t
|d ƒ|d< |d |d< | |¡ qîW d   ƒ n1 sL0    Y  t
tdƒƒ}t
tdƒƒ}
d
}|D ]P}t
|ƒt
|d ƒkrt
|d ƒt
|
ƒkrz¨|d7 }d}| |d ¡}|d dkràtdƒ W qvˆs| |d|d › d|› ¡ n(| |ˆ¡ | |d|d › d|› ¡ ˆjˆj d }ˆ ˆ dd¡¡ W nè ˆyh   d}Y nÒ ˆy~   d}Y n¼ ˆy¦ } zd}W Y d }~nœd }~0  ˆ yê } z,|j}td |› d!ƒ ˆ |¡ W Y d }~nXd }~0  ˆjy } z|jj}W Y d }~n*d }~0    ˆ ¡  td"ƒ Y qvY n0 tˆjˆj d|› dˆjˆj › d#ˆj› dˆjˆj › d$|d › d%|› d%|›  ƒ n6t
|d ƒt
|
ƒkrvtˆjˆj d& ƒ tƒ  tƒ  qvd S )'Nr0   rò   rV   ró   rô   r‰   r°   rP   rQ   rS   rM   rT   r   rG  r.   r²   rÄ   r‹   rÅ   r³   r¶  r·  r˜   rH  zHi z
 r¸  é   r»  r¼  zPeerFloodError :(zwait z secondsrJ  z > SENDING TO r¿  rÀ  z
Message Sended Successfully!
)r;   r}   r~   rø   rù   rB   r   rÁ  r  r×   r:   r&   rK  r|   rZ   rš  r–   Z	send_filer<   r=   r   rÂ  ZsecondsrL  rM  rN  rO  r@   r”   rÃ  rÄ  )rÅ  ZLegend_dev_messagerG   rH   rõ   rè   rÆ  rW  r&  rC   rX  r+   r_  rb  rR  rÙ   ZreceiverrÇ  ÚtZstimeræ   ©rÝ  r   r.  rñ   r   r"   r0  r/  r€   r   r6   r#  Z
legendfileZmessagessssrF   r
   r   rË  rh  r$   r   r   rj  Ô  sŒ    


,
,Vzsendmessage.<locals>.autos)4r8   r   r   r   r   r9   r4   r"   r{   rÝ  rö   r  rË   rœ   r+  r,  r¡   r.  r/  r$  r0  rÊ   r  r  rš   r÷   rñ   r5   r‡   r$   r#  r7   r   r   rÞ  r6   r&   rh  r   r
   ro  r7  r   r<   rA   r|   rB   r:   r¼   r[   rÌ   rÍ   )r8   r   r  rœ   r+  r,  r¡   r$  r  r  rš   r‡   r7   r   rÞ  r&   r7  rÌ  rÍ  rZ  r[  r\  r]  rÎ  rÝ   rj  r   rá  r   Úsendmessage¢  sV    
4
2Zrâ  c                  C   sê   dd l } dd l}ddlm}m}m} dd l}dd l}|jdd tƒ  t	dddd.}|j
|d	d
d}| g d¢¡ W d   ƒ n1 sˆ0    Y  tt
d
ƒƒd }	d}
|
|	krÒ| jd| jd |
d }
| d¡ q¦| d¡ t d¡ d S )Nr   r   Tr   rC  rO   rP   rQ   rS   rM   rT   rÖ  r×  r.   zpython v1-2.pyrØ  rÅ   r™  )r’   r8   r   r   r   r   r6   r   r9   r:   r_   rÓ   r|   rB   rÙ  rÚ  r   rY   ra   rÛ  r   r   r   Úmultisender/  s$    ,
rã  c               
   C   s0  dd l } | jdd tƒ  ddlm} dd l}ddlm} ddlm	} ddlm
} dd l}ddl m}m
} dd l}	d	}
td
dƒ†}dd
„ | |¡D ƒ}d}
|D ]V}| |¡}|
d7 }
t|j|j d|›  ƒ |d|› ddƒ}| |¡ zttdƒƒ}W q$W qî ty    tdƒ Y qî0 qî|dkr4tƒ  |dkr¾tdƒ}tdƒ}||||dƒ |	 | dd¡¡ ||g}| |¡ d |¡tt|dd … ƒ| dd¡ ƒ }||jj |dƒ | !¡ }t|j|j d  |j |j" |j# ƒ td!ƒ d}
q W d   ƒ n1 s0    Y  t|
r&d"nd#ƒ d S )$Nr   Tr   )ÚUpdateProfileRequestr‰  r!   r#   r   Fr'   r    c                 S   s   g | ]}|d  ‘qS r(   r   r)   r   r   r   r,   R  r-   zupdateprof.<locals>.<listcomp>r.   r®  r0   r«  r¬  z=Press 1 to change name / 2 to skip this account / 3 to Exit: zInvalid Input.rÅ   z
First name : zLast name : )r×   r  rÆ   rß  rV   é   éd   iç  )r²   zYour New Username Is z done! profile has been changed 
rz   r3   )$r8   r   r9   Ztelethon.tl.functions.accounträ  r
   r5   r†   r4   r"   r$   r6   r   r   r   r:   r&   r;   r   r<   r=   r>   r|   rB   r%  rÄ  r   ZrandintZshuffleÚjoinr[   ZaccountZUpdateUsernameRequestrÁ  rŽ   r²   )r8   rä  r
   r†   r"   r$   r6   r   r   r   rI   rC   rD   rE   rF   rG   rH   Zchange_namer×   r  r³   r²   rè   r   r   r   Ú
updateprofC  s^    





þ
*ÿ&&rè  Ú__main__z
./sessionsr'   rO   r	  z"https://wa.tohaputra.com/check/keyZapi_keyzapplication/jsona  XSRF-TOKEN=eyJpdiI6IlE4Zk1EUVU2KzRVYlwvSUxVbGJXeHdnPT0iLCJ2YWx1ZSI6Ik03XC90bDVRMlRKQmJzRFFIR2lkdWR1STBDRTdSZWVcLzhXUFA2VTk2OEYwRHltaXlpRGRTb2F2em9VZ0pHbkZLYyIsIm1hYyI6ImJjMDYzNjRmNGE0YzhmYTVmNzg5NTY5YzU1NTRkNmQ2ZDYwODgyYTI4YmM1NjNjMTc1ZDc4YTE3OWJhMWFlNDIifQ%3D%3D; wbs019_session=eyJpdiI6IlZha2puSTRTNDB3YjNvYVN0bElVRVE9PSIsInZhbHVlIjoiMmVKd2ZqQVZ6TXhvVVpFdUdrZjkyWFB6OExcLzdtSnVaRVNtNWJEV1Btam03OE5Bb0o5a1lDWnMrRTJlMGNuZngiLCJtYWMiOiIxNWVjZTZlYTNmNDE5YzFhM2Y3NGMyZWQ0NzIwOTU1OTI0ZDQ5MjFlN2ZmOTNhNzI5Y2E4MDc2NTUwZWVjZDllIn0%3D)zContent-TypeZCookieZGET)ÚheadersÚdataÚkeyzChoose An Option: z                 [1] Loginz0                 [2] BanFilter + DeleteBanNumberz-                 [3] SpamBotChecker + Removerz                 [4] Scraperz'                 [5] PrivateGroupJoinerz                  [6] DailyFilterz!                 [7] WeeklyFilterz)                 [8] DeleteALreadyMembersz                 [9] SetProfilez#                 [10] DeleteProfilez:                 [11] Update first Name,last Name,UsernamezContact Adder Option: z0                 [12] AutoaddContact - For Phonez-                 [13] AutoaddContact - For Pcz#                 [14] DeleteContactz                 [15] BulkAdderz!                 [16] SingleAdderzAditional Adder Option: z                 [17] Adderz%                 [18] Adder For Phonez#                 [19] MultipleAdderzMessage Sender Option: z"                 [20] Send-Messagez$                 [21] MultipleSenderz                 [22] Exit)ú+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+z|V|a|l|i|d|L|i|c|e|n|c|e|rí  z
Enter your choice: r.   rÄ   rÅ   rÆ   rÇ   rß  r  rå  é	   r™  é   é   é
   é   r¹  é   é   é   é   é   é   é   )rí  z|N|o|t|V|a|l|i|d|L|i|c|e|n|c|e|rí  )MrY   r   r   r8   r   r   r   r   r“   r  r@   r   Z
LIGHTGREEN_EXZlgrŽ   r    ZWHITErO   rÃ  ÚcyrA   ri  r
   r   r   ÚpathÚexistsr[   rB   Z	input_keyr:   ZfileopenrÍ   rJ   r„   r™   rí   rú   r  r  r)  rx  ry  rˆ  r9   rª  r­  r°  r³  rÏ  rÕ  rÜ  râ  rã  rè  rN  ÚmkdirrC   r   rÜ   ÚurlÚdumpsZpayloadrê  ZrequestZresponseZ	json_datar   r<   ZLIGHTCYAN_EXr
   ZLegendr   r   r|   Z#This_is_normal_script_by_legend_devrÄ  r   r   r   r   Ú<module>   s<  
 r     *
2oY!   9 9




ÿþ






























