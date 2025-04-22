<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output encoding="UTF-8" indent="yes" method="html"/>
    <xsl:template match="/universidad">
        <alumnos universidad="{nombre}"
                 numTitulos ="{count(carreras/carrera)}"
                 numCreditos="{sum(carreras/carrera/creditos)}"
                 numAlumnos="{count(alumnos/alumno)}">
            <observaciones>Estadística asignaturass por alumnos</observaciones>              
     
        <xsl:apply-templates select="alumnos/alumno"/>
        </alumnos>
           </xsl:template>
        <xsl:template match="alumno">
            <alumno nombre="{@id}" 
                    codigoGrado="{estudios/carrera/@codigo}" 
                    carrera="{@carrera}" 
                    numeroAsignaturas="{count(estudios/asignaturas/asignatura)}"/>
        </xsl:template>
    
</xsl:stylesheet>