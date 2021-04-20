import { Component, OnInit } from '@angular/core';
import { Webcam } from '../webcam';
import { WEBCAMS } from '../mock-webcams';

@Component({
		selector: 'app-webcams',
		templateUrl: './webcams.component.html',
		styleUrls: ['./webcams.component.css']
})
export class WebcamsComponent implements OnInit {
		
		constructor() { }
		
		ngOnInit(): void {
		}

		webcams = WEBCAMS;

}
