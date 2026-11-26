// Usage: npm install playwright pdf-lib && npx playwright install chromium
// node pdf.cjs input.html output.pdf
const { chromium } = require(process.env.VAIMURAAMAT_PLAYWRIGHT || 'playwright');
const { pathToFileURL } = require('url');
const path = require('path');
const fs = require('fs');
const {PDFDocument, rgb} = require(process.env.VAIMURAAMAT_PDFLIB || 'pdf-lib');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
 const page=await browser.newPage();
 await page.goto(pathToFileURL(path.resolve(process.argv[2])).href,{waitUntil:'load'});
 await page.evaluate(()=>document.fonts.ready);
 const pdfBytes=await page.pdf({format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<div style="width:100%;margin:0 20.5mm;display:flex;justify-content:space-between;font:8pt Arial;color:#647080"><span>VAIMURAAMAT</span><span>Punkt A</span></div>',footerTemplate:'<div style="width:100%;margin:0 20.5mm;border-top:0.5pt solid #57A7B3;padding-top:7pt;display:flex;justify-content:space-between;font:8pt Arial;color:#647080"><span>Vaimuraamat</span><a href="https://vaimuraamat.ee/" style="color:#192B43;text-decoration:none">vaimuraamat.ee</a><span class="pageNumber"></span></div>'});
 const pdf=await PDFDocument.load(pdfBytes);
 const pages=pdf.getPages(),n=pages.length;
 pages.forEach((p,i)=>{const {width,height}=p.getSize(),bar=6*72/25.4;
 p.drawRectangle({x:width-bar,y:0,width:bar,height,color:rgb(239/255,246/255,246/255)});
 p.drawRectangle({x:width-bar,y:height*(n-i-1)/n,width:bar,height:height/n,color:rgb(236/255,106/255,135/255)});
 });
 fs.writeFileSync(process.argv[3],await pdf.save());
 }finally{await browser.close();}
})();
