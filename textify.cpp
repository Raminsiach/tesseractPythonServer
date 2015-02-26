//
//  textify.cpp
//  main
//
//  Created by Ramin Siahcheshmi on 2/22/15.
//  Copyright (c) 2015 Ramin. All rights reserved.
//

#include "textify.h"

const char *textify(const char *filepath) {
    const char *outText;
    
    tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
    // Initialize tesseract-ocr with English, without specifying tessdata path
    if (api->Init(NULL, "eng")) {
        fprintf(stderr, "Could not initialize tesseract.\n");
        exit(1);
    }
    
    // Open input image with leptonica library
    Pix *image = pixRead(filepath);
    api->SetImage(image);
    // Get OCR result
    outText = api->GetUTF8Text();
    
    
    // Destroy used object and release memory
    api->End();
    delete [] outText;
    pixDestroy(&image);

    return outText;
}
